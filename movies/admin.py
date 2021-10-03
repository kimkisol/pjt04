from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    display = [
        'pk',
        'title',
        'overview',
        'poster_path',
    ]

admin.site.register(Movie, MovieAdmin)