from core.models import User


def update_user(user: User, **kwargs) -> User:
    for field_name, field_value in kwargs.items():
        if field_name == 'password':
            user.set_password(raw_password=field_value)
            continue
        setattr(user, field_name, field_value)
    user.save()
    return user


def create_user(**kwargs) -> User:
    raw_password = kwargs.pop('password', None)
    user = User.objects.create(**kwargs)
    user.set_password(raw_password=raw_password)
    user.save()
    return user
