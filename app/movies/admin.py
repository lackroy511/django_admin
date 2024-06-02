from django.contrib import admin

from app.movies.models import FilmWork


# Register your models here.
@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    pass
