from django.contrib.auth.hashers import make_password
from auth.models import User


seed_items = [
    User(
        pk=1,
        email='admin@example.com',
        name='Admin',
        username='admin',
        password=make_password('admin'),
        is_staff=True,
        is_superuser=True,
        is_admin=True,
    ),
    User(
        pk=2,
        email='jon@snow.com',
        name='Jon Snow',
        username='jonsnow',
        password=make_password('pass4user'),
        is_admin=True,
    ),
    User(
        pk=3,
        email='harry@potter.com',
        name='Harry Potter',
        username='harry',
        password=make_password('pass4user'),
        is_admin=True,
    ),
    User(
        pk=4,
        email='frodo@baggins.com',
        name='Frodo Baggins',
        username='frodo',
        password=make_password('pass4user'),
    ),
    User(
        pk=5,
        email='tony@stark.com',
        name='Tony Stark',
        username='tony',
        password=make_password('pass4user'),
    ),
]
