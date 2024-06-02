from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
import uuid


class Genre(TimeStampedModel):
    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Person(TimeStampedModel):
    class Meta:
        verbose_name = _('персона')
        verbose_name_plural = _('персоны')
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(_('Дата рождения'), auto_now=False, blank=True, null=True)
    

class FilmWork(TimeStampedModel):
    class Meta:
        verbose_name = _('фильм')
        verbose_name_plural = _('фильмы')
        
    class FilmType(models.TextChoices):
        MOVIE = 'movie', _('фильм')
        TV_SHOW = 'tv_show', _('ТВ шоу')
        SERIES = 'series', _('сериал')
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(_('Название'))
    description = models.TextField(_('Описание'), null=True, blank=True)
    creation_date = models.DateField(_('Дата создания'), auto_now=False, auto_now_add=False)
    age_rating = models.CharField(_('Возрастной рейтинг'), max_length=10, null=True, blank=True)
    film_type = models.TextField(_('Тип'), choices=FilmType.choices, default=FilmType.MOVIE)
    file_path = models.TextField(_('Путь к файлу'), null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name=_('жанр'), related_name='genre')
    director = models.ManyToManyField(Person, verbose_name=_('режиссер'), related_name='film_director')
    actor = models.ManyToManyField(Person, verbose_name=_('актер'), related_name='film_actor')
    writer = models.ManyToManyField(Person, verbose_name=_('сценарист'), related_name='film_writer')
    test_field = models.TextField(_('qwe'), null=True, blank=True)
