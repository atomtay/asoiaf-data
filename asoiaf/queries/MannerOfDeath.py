
from django.db import connection


def get_data(self):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT count(character_id) FROM death_manner WHERE manner!='Unknown' GROUP BY manner ORDER BY count(character_id) DESC LIMIT 10;")
        data = cursor.fetchall()

    return data


def get_providers(self):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT manner FROM death_manner WHERE manner!='Unknown' GROUP BY manner ORDER BY count(character_id) DESC LIMIT 10;")
        providers = cursor.fetchall()

    return providers
