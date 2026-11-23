from django.contrib import admin

from .models import Movie

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['name','genre','director','actor','actress','rdate','language','rating']

admin.site.register(Movie,MoviesAdmin)
