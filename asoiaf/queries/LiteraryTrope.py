from django.db import connection


def get_data(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT num_of_chapters FROM books;")
        chapter_list = []
        for chapter in cursor.fetchall():
            chapter_list.append(chapter[0])

        cursor.execute("SELECT ROUND(AVG(death_chapter.chapter)) FROM characters INNER JOIN death_chapter ON characters.id=death_chapter.character_id INNER JOIN death_book ON death_book.character_id=death_chapter.character_id WHERE characters.gender='Male' GROUP BY death_book.book_id ORDER BY death_book.book_id ASC;")

        male_chapter_list = []
        for chapter in cursor.fetchall():
            male_chapter_list.append(chapter[0])

        cursor.execute("SELECT ROUND(AVG(death_chapter.chapter)) FROM characters INNER JOIN death_chapter ON characters.id=death_chapter.character_id INNER JOIN death_book ON death_book.character_id=death_chapter.character_id WHERE characters.gender='Female' GROUP BY death_book.book_id ORDER BY death_book.book_id ASC;")

        female_chapter_list = []
        for chapter in cursor.fetchall():
            female_chapter_list.append(chapter[0])
    return [chapter_list, male_chapter_list, female_chapter_list]
