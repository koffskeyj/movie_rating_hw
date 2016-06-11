from django.shortcuts import render
from movierating.models import Rating, Rater, Movie


def movie_index(request, movie_id):
    Movie_dict = {
        "movies": list(Movie.objects.filter(movie_title__contains=movie_id)),
        "ratings": list(Rating.objects.filter(item_id__con=movie_id))
    }

    return render(request, "Movies.html", Movie_dict)


def rating_index(request):
    Rating_dict = {
        "ratings": list(Rating.objects.all()),
        "movies": list(Movie.objects.all()),
        "raters": list(Rater.objects.all())
    }

    return render(request, "Rating.html", Rating_dict)

def rater_index(request, rater_id):
    Rater_dict = {
        "raters": list(Rater.objects.filter(id=rater_id)),
        "ratings": list(Rating.objects.filter(user_id=rater_id))
    }

    return render(request, "Users.html", Rater_dict)