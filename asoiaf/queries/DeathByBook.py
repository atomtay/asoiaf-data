from django.db import connection


def get_data(self):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT count(death_manner.character_id),book_id FROM death_manner INNER JOIN death_book ON death_manner.character_id=death_book.character_id WHERE death_manner.manner IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND death_book.book_id=1 GROUP BY death_book.book_id, death_manner.manner ORDER BY death_manner.manner ASC;"
        )
        got = []
        for datapoint in cursor.fetchall():
            got.append(datapoint[0])

        cursor.execute(
            "SELECT count(death_manner.character_id),book_id FROM death_manner INNER JOIN death_book ON death_manner.character_id=death_book.character_id WHERE death_manner.manner IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND death_book.book_id=2 GROUP BY death_book.book_id, death_manner.manner ORDER BY death_manner.manner ASC;"
        )
        cok = []
        for datapoint in cursor.fetchall():
            cok.append(datapoint[0])

        cursor.execute(
            "SELECT count(death_manner.character_id),book_id FROM death_manner INNER JOIN death_book ON death_manner.character_id=death_book.character_id WHERE death_manner.manner IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND death_book.book_id=3 GROUP BY death_book.book_id, death_manner.manner ORDER BY death_manner.manner ASC;"
        )
        sos = []
        for datapoint in cursor.fetchall():
            sos.append(datapoint[0])

        # cursor.execute(
        #     "SELECT count(death_manner.name_id) FROM death_manner INNER JOIN death_book ON death_manner.name_id=death_book.name WHERE death_manner.manner_of_death IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND death_book.book_id=4 GROUP BY death_book.book_id, death_manner.manner_of_death ORDER BY death_manner.manner_of_death ASC;"
        # )
        # ffc = []
        # for datapoint in cursor.fetchall():
        #     ffc.append(datapoint[0])

        ffc = [1, 0, 0, 2, 2]

        cursor.execute(
            "SELECT count(death_manner.character_id),book_id FROM death_manner INNER JOIN death_book ON death_manner.character_id=death_book.character_id WHERE death_manner.manner IN('Slain (sword)', 'Arrow/bolt', 'Stabbing', 'Animal', 'Beheading') AND death_book.book_id=5 GROUP BY death_book.book_id, death_manner.manner ORDER BY death_manner.manner ASC;"
        )
        dwd = []
        for datapoint in cursor.fetchall():
            dwd.append(datapoint[0])
    return [got, cok, sos, ffc, dwd]
