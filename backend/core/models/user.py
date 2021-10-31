import os
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from hashlib import pbkdf2_hmac
from django.db import models
from core.utils import validate_raw_password


class User(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=100,
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
        max_length=150,
        unique=True,
        validators=[
            UnicodeUsernameValidator()
        ],
    )
    password = models.CharField(
        verbose_name='password',
        max_length=150
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
        password_salt = self.password[:self.PASSWORD_SALT_SIZE]
        password_key = self.password[self.PASSWORD_SALT_SIZE:]
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
