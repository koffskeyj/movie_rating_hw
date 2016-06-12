from django.shortcuts import render
from movierating.models import Rating, Rater, Movie
from django.db.models import Avg
from django.db.models import Max


def movie_index(request, movie_id):
    Movie_dict = {
        "movies": list(Movie.objects.filter(id=movie_id)),
        "ratings": list(Rating.objects.filter(item_id=movie_id)),
        "average": Rating.objects.filter(item_id=movie_id).aggregate(Avg('rating'))
    }

    return render(request, "Movies.html", Movie_dict)


def top20_rating_index(request):

    Rating_dict = {
        "average_all": list(Rating.objects.values_list('item_id').annotate(Avg('rating')))

    }

    return render(request, "Rating.html", Rating_dict)


def rater_index(request, rater_id):
    Rater_dict = {
        "raters": list(Rater.objects.filter(id=rater_id)),
        "ratings": list(Rating.objects.filter(user_id=rater_id))
    }

    return render(request, "Users.html", Rater_dict)