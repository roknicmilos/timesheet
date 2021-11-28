import os
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from hashlib import pbkdf2_hmac
from django.db import models
from core.models.base import BaseModel, BaseManager
from core.utils import validate_raw_password


class UserManager(BaseManager):

    def create(self, **kwargs):
        raw_password = kwargs.pop('password', None)
        user = super(UserManager, self).create(**kwargs)
        user.set_password(raw_password=raw_password)
        user.save()
        return user


class User(BaseModel):
    objects = UserManager()

    name = models.CharField(
        verbose_name='name',
        max_length=250,
        validators=[
            MinLengthValidator(limit_value=4)
        ]
    )
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=250,
        unique=True,
        validators=[
            UnicodeUsernameValidator()
        ],
    )
    password = models.BinaryField(
        verbose_name='password',
        max_length=500,
        default=b'',
    )
    weekly_hours = models.FloatField(
        verbose_name='weekly hours'
    )
    is_active = models.BooleanField(
        verbose_name='is active',
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name='is admin',
        default=False,
    )

    PASSWORD_SALT_SIZE = 32
    PASSWORD_ALGORITHM = 'sha256'
    PASSWORD_HASH_ITERATIONS = 100000

    def set_password(self, raw_password: str) -> None:
        validate_raw_password(raw_password=raw_password)
        password_salt = os.urandom(self.PASSWORD_SALT_SIZE)
        password_key = pbkdf2_hmac(
            hash_name=self.PASSWORD_ALGORITHM,
            password=raw_password.encode('utf-8'),
            salt=password_salt,
            iterations=self.PASSWORD_HASH_ITERATIONS
        )
        self.password = password_salt + password_key


    def check_password(self, raw_password) -> bool:
        if not (isinstance(raw_password, str) and self.password):
            return False

        original_password = bytes(self.password)
        password_salt = original_password[:self.PASSWORD_SALT_SIZE]
        password_key = original_password[self.PASSWORD_SALT_SIZE:]
        other_password_key = pbkdf2_hmac(
            hash_name=self.PASSWORD_ALGORITHM,
            password=raw_password.encode('utf-8'),
            salt=password_salt,
            iterations=self.PASSWORD_HASH_ITERATIONS
        )

        return password_key == other_password_key


    @property
    def is_worker(self) -> bool:
        return not self.is_admin

    def update(self, **kwargs):
        raw_password = kwargs.pop('password', None)
        if raw_password:
            self.set_password(raw_password=raw_password)
        return super(User, self).update(**kwargs)
