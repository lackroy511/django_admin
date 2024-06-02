from django.shortcuts import render

# Create your views here.
from dal import autocomplete
from .models import Genre, Actor, Director


class GenreAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor!
        if not self.request.user.is_authenticated:
            return Genre.objects.none()

        qs = Genre.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class ActorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Actor.objects.none()

        qs = Actor.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class DirectorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Director.objects.none()

        qs = Director.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
