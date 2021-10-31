import os
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from hashlib import pbkdf2_hmac
from core.models.base import BaseModel
from core.utils import validate_raw_password, mask_string


class User(BaseModel):
    name: str
    email: str
    username: str
    weekly_hours: float = 0
    is_active: bool = True
    is_admin: bool = False

    _password_salt: bytes
    _password_key: bytes

    PASSWORD_ALGORITHM = 'sha256'
    PASSWORD_HASH_ITERATIONS = 100000

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.username = kwargs.get('username')
        raw_password = kwargs.get('password')
        if raw_password:
            self.password = raw_password

    @property
    def password(self) -> str:
        return f'algorithm: {self.PASSWORD_ALGORITHM} ' \
               f'iterations: {self.PASSWORD_HASH_ITERATIONS} ' \
               f'salt: {mask_string(self.password_salt)} ' \
               f'hash: {mask_string(self.password_key)}'

    @password.setter
    def password(self, raw_password: str) -> None:
        validate_raw_password(raw_password=raw_password)
        self._password_salt = os.urandom(32)
        self._password_key = pbkdf2_hmac(
            hash_name=self.PASSWORD_ALGORITHM,
            password=raw_password.encode('utf-8'),
            salt=self._password_salt,
            iterations=self.PASSWORD_HASH_ITERATIONS
        )

    @property
    def password_salt(self) -> str:
        return self._password_salt.decode("utf-8")

    @property
    def password_key(self) -> str:
        return self._password_key.decode("utf-8")

    def check_password(self, raw_password) -> bool:
        password_key = pbkdf2_hmac(
            hash_name=self.PASSWORD_ALGORITHM,
            password=raw_password.encode('utf-8'),
            salt=self._password_salt,
            iterations=self.PASSWORD_HASH_ITERATIONS
        )
        return password_key == self._password_key


    @property
    def is_worker(self) -> bool:
        return not self.is_admin

    def validate(self) -> None:
        errors = {}
        try:
            self._validate_username()
        except ValidationError as error:
            errors['username'] = error.message

        try:
            validate_email(self.email)
        except ValidationError:
            errors['email'] = 'Invalid email'

        try:
            self._validate_name()
        except ValidationError as error:
            errors['name'] = error.message

        if errors:
            raise ValidationError(errors)

    def _validate_name(self) -> None:
        if not self.name:
            raise ValidationError('Name must be provided')


    def _validate_username(self) -> None:
        if self.username is None or self.username == '':
            raise ValidationError('Username must be provided')
        if not isinstance(self.username, str):
            raise ValidationError('Username must be a string')
        if len(self.username) < 4:
            raise ValidationError('Username must have at least 4 characters')
