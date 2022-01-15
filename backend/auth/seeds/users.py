from auth.models import User


seed_items = [
    User(
        pk=1,
        email='admin@example.com',
        name='Admin',
        username='admin',
        is_staff=True,
        is_superuser=True,
        is_admin=True,
    ),
    User(
        pk=2,
        email='jon@snow.com',
        name='Jon Snow',
        username='jonsnow',
        is_admin=True,
    ),
    User(
        pk=3,
        email='harry@potter.com',
        name='Harry Potter',
        username='harry',
        is_admin=True,
    ),
    User(
        pk=4,
        email='frodo@baggins.com',
        name='Frodo Baggins',
        username='frodo',
    ),
    User(
        pk=5,
        email='tony@stark.com',
        name='Tony Stark',
        username='tony',
    ),
]


def post_seed():
    for seed in seed_items:
        user = User.objects.get(pk=seed.pk)
        user.set_password('pass4user')
        user.save()
