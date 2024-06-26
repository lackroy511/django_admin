# Generated by Django 5.0.6 on 2024-06-02 09:45

import django.utils.timezone
import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'персона',
                'verbose_name_plural': 'персоны',
            },
        ),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('creation_date', models.DateField(verbose_name='Дата создания')),
                ('age_rating', models.CharField(blank=True, max_length=10, null=True, verbose_name='Возрастной рейтинг')),
                ('film_type', models.TextField(choices=[('movie', 'фильм'), ('tv_show', 'ТВ шоу'), ('series', 'сериал')], default='movie', verbose_name='Тип')),
                ('file_path', models.TextField(blank=True, null=True, verbose_name='Путь к файлу')),
                ('genre', models.ManyToManyField(related_name='genre', to='movies.genre', verbose_name='жанр')),
                ('actor', models.ManyToManyField(related_name='film_actor', to='movies.person', verbose_name='актер')),
                ('director', models.ManyToManyField(related_name='film_director', to='movies.person', verbose_name='режиссер')),
                ('writer', models.ManyToManyField(related_name='film_writer', to='movies.person', verbose_name='сценарист')),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'фильмы',
            },
            
        ),
        migrations.RunSQL('CREATE UNIQUE INDEX IF NOT EXISTS film_work_genre_index ON movies_filmwork_genre (filmwork_id, genre_id);'),
        migrations.RunSQL('CREATE UNIQUE INDEX IF NOT EXISTS film_work_actor_index ON movies_filmwork_actor (filmwork_id, person_id);'),
        migrations.RunSQL('CREATE UNIQUE INDEX IF NOT EXISTS film_work_director_index ON movies_filmwork_director (filmwork_id, person_id);'),
        migrations.RunSQL('CREATE UNIQUE INDEX IF NOT EXISTS film_work_writer_index ON movies_filmwork_writer (filmwork_id, person_id);'),
    ]
