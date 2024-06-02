import psycopg2
from psycopg2.extras import execute_batch
import random
from datetime import date, datetime
import pytz
import uuid
import os

PSQL_DSN = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
}


def main():
    # fill_film_work_table()
    # fill_genres_table()
    fill_person_table()


def fill_film_work_table():
    counter = 0
    data = []
    for i in range(300):
        for i in range(10000):
            movie_data = {
                'id': str(uuid.uuid4()),
                'title': f'mov_try_3_{counter}',
                'description': f'description_try_3_{counter}',
                'creation_date': date.today().strftime('%Y-%m-%d'),
                'age_rating': f'{random.randint(3, 21)}+',
                'film_type': 'movie',
                'file_path': None,
                'rating': round(random.uniform(0.0, 10.0), 1),
                'created': datetime.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
                'modified': datetime.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
            }
            data.append(tuple(movie_data.values()))
            counter += 1

        with psycopg2.connect(**PSQL_DSN) as conn:
            with conn.cursor() as cursor:
                execute_batch(
                    cursor, 
                    'INSERT INTO movies_filmwork (id, title, description, creation_date, age_rating, film_type, file_path, rating, created, modified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON conflict(id) DO NOTHING;', 
                    data,
                    page_size=10000)
                conn.commit()


def fill_genres_table():
    counter = 0
    data = []
    for i in range(10000):
        movie_data = {
            'id': str(uuid.uuid4()),
            'name': f'genre_{counter}',
            'description': f'description_{counter}',
            'created': datetime.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
            'modified': datetime.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
        }
        data.append(tuple(movie_data.values()))
        counter += 1

    with psycopg2.connect(**PSQL_DSN) as conn:
        with conn.cursor() as cursor:
            execute_batch(
                cursor, 
                'INSERT INTO movies_genre (id, name, description, created, modified) VALUES (%s, %s, %s, %s, %s);', 
                data,
                page_size=10000)
            conn.commit()


def fill_person_table():
    counter = 0
    data = []
    for i in range(5500):
        movie_data = {
            'id': str(uuid.uuid4()),
            'name': f'person_{counter}',
            'birth_date': date.today().strftime('%Y-%m-%d'),
            'created': datetime.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
            'modified': datetime.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
        }
        data.append(tuple(movie_data.values()))
        counter += 1

    with psycopg2.connect(**PSQL_DSN) as conn:
        with conn.cursor() as cursor:
            execute_batch(
                cursor, 
                'INSERT INTO movies_person (id, name, birth_date, created, modified) VALUES (%s, %s, %s, %s, %s);', 
                data,
                page_size=10000)
            conn.commit()


if __name__ == '__main__':
    main()
