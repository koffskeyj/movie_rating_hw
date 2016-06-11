from django.contrib import admin

from movierating.models import Rater, Movie, Rating

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)

