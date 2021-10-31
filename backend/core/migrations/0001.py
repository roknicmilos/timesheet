from django.db import migrations
from main.settings import BASE_DIR


create_tables_sql_file_path = f'{BASE_DIR}/core/migrations/create_tables.sql'
with open(create_tables_sql_file_path) as file:
    sql = ''.join(file.readlines())

drop_tables_sql_file_path = f'{BASE_DIR}/core/migrations/drop_tables.sql'
with open(drop_tables_sql_file_path) as file:
    reverse_sql = ''.join(file.readlines())


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql),
    ]
