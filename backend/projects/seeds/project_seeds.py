import random
from auth.models import User
from projects.models import Project, Client

seed_items = []

latest_project_pk = 1
for client in Client.objects.all():
    first_project = Project(
        pk=latest_project_pk,
        client=client,
        name=f'First {client.name} project',
        description=f'First project for the client {client.name}',
        lead_employee=User.objects.filter(pk=random.randint(1, 5)).first(),
        is_archived=True,
    )

    latest_project_pk += 1
    second_project = Project(
        pk=latest_project_pk,
        client=client,
        name=f'Second {client.name} project',
        description=f'Second project for the client {client.name}',
        lead_employee=User.objects.filter(pk=random.randint(1, 5)).first(),
        is_active=True,
    )
    latest_project_pk += 1

    seed_items.extend([
        first_project,
        second_project,
    ])
