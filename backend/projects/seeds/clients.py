from projects.models import Client

seed_items = [
    Client(
        pk=1,
        name="Coca Cola",
        street="7th street",
        city="New York",
        country="USA",
        zip_code=10001
    ),
    Client(
        pk=2,
        name="Tesla",
        street="8th street",
        city="Los Angeles",
        country="USA",
        zip_code=90001
    ),
    Client(
        pk=3,
        name="Space X",
        street="9th street",
        city="Chicago",
        country="USA",
        zip_code=60007
    ),
    Client(
        pk=4,
        name="Plazma",
        street="Nikole Tesle",
        city="Beograd",
        country="Srbija",
        zip_code=101801
    ),
    Client(
        pk=5,
        name="Matijević",
        street="Novosadskog sajma",
        city="Novi Sad",
        country="Srbija",
        zip_code=21000
    ),
]
