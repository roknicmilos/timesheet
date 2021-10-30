from django.db import migrations

sql_query = """
    CREATE TABLE core_daily_time_sheet (
       id INTEGER NOT NULL PRIMARY KEY, 
       date DATE NOT NULL, 
       user_id INTEGER NOT NULL, 
       CONSTRAINT fk_user
            FOREIGN KEY(user_id)
                REFERENCES core_user(id)
                ON DELETE CASCADE 
    );
"""

reverse_sql_query = 'DROP TABLE core_daily_time_sheet;'


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_user'),
    ]

    operations = [
        migrations.RunSQL(sql_query, reverse_sql_query),
    ]
