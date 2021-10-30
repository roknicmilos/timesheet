from django.db import migrations

sql_query = """
    CREATE TABLE core_user (
       id INTEGER NOT NULL PRIMARY KEY, 
       name VARCHAR(250) NOT NULL, 
       weekly_hours FLOAT NOT NULL, 
       username VARCHAR(250) NOT NULL, 
       email VARCHAR(250) NOT NULL, 
       is_active BOOLEAN NOT NULL, 
       is_admin BOOLEAN NOT NULL
    );
"""

reverse_sql_query = 'DROP TABLE core_user;'


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(sql_query, reverse_sql_query),
    ]
