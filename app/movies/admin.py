from django.contrib import admin

from movies.models import FilmWork, Genre, Person


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'age_rating', 'film_type', 'rating')
    search_fields = ('title', 'creation_date', 'film_type', 'rating')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name', 'birth_date')
