from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Genre(TimeStampedModel):
    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')

    name = models.CharField(_('название'), max_length=255)
    description = models.CharField(_('описание'), max_length=50)

    def __str__(self):
        return self.name


class FilmWorkType(models.TextChoices):
    MOVIE = 'movie', _('фильм')
    TV_SHOW = 'tv_show', _('шоу')


class FilmWork(TimeStampedModel):
    class Meta:
        verbose_name = _('кинопроизведение')
        verbose_name_plural = _('кинопроизведения')

    title = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)
    creation_date = models.DateField(_('дата создания фильма'), blank=True)
    certificate = models.TextField(_('сертификат'), blank=True)
    file_path = models.FileField(_('файл'), upload_to='film_works/', blank=True)
    rating = models.FloatField(_('рейтинг'), validators=[MinValueValidator(0)], blank=True)
    type = models.CharField(_('тип'), max_length=20, choices=FilmWorkType.choices)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
