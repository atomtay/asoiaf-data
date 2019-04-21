from django.db import connection


def get_data(self):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT count(name) from characters WHERE gender='Male';")
        total_males = cursor.fetchone()[0]

        cursor.execute(
            "SELECT count(name) from characters WHERE gender='Female';")
        total_females = cursor.fetchone()[0]

        cursor.execute(
            "SELECT count(name) from characters INNER JOIN death_manner ON characters.id=death_manner.character_id WHERE characters.gender = 'Male';")
        male_deaths = cursor.fetchone()[0]

        cursor.execute(
            "SELECT count(name) from characters INNER JOIN death_manner ON characters.id=death_manner.character_id WHERE characters.gender = 'Female';")
        female_deaths = cursor.fetchone()[0]

        alive_males = total_males-male_deaths
        alive_females = total_females-female_deaths

        return [[total_males, alive_males, male_deaths],
                [total_females, alive_females, female_deaths]]
