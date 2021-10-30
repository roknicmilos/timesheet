from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from core.models.base import BaseModel


class User(BaseModel):
    name: str
    email: str
    username: str
    password: str
    weekly_hours: float = 0
    is_active: bool = True
    is_admin: bool = False

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.name = kwargs.get('name')

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

    def _validate_email(self) -> None:
        validate_email(self.email)

    def _validate_username(self) -> None:
        if self.username is None or self.username == '':
            raise ValidationError('Username must be provided')
        if not isinstance(self.username, str):
            raise ValidationError('Username must be a string')
        if len(self.username) < 4:
            raise ValidationError('Username must have at least 4 characters')
