from django.shortcuts import render
from movierating.models import Rating, Rater, Movie
from django.db.models import Avg


def movie_index(request, movie_id):
    Movie_dict = {
        "movies": list(Movie.objects.filter(id=movie_id)),
        "ratings": list(Rating.objects.filter(item_id=movie_id)),
        "average": Rating.objects.filter(item_id=movie_id).aggregate(avg_rating = Avg('rating'))
    }

    return render(request, "Movies.html", Movie_dict)


def top20_rating_index(request):

    Rating_dict = {
        "average_all": Rating.objects.values('item_id__movie_title').annotate(ratings = Avg('rating')).order_by('-ratings')[:20],
        "average_item": Rating.objects.values('item_id').annotate(ratings = Avg('rating')).order_by('-ratings')[:20]
    }

    return render(request, "Rating.html", Rating_dict)


def rater_index(request, rater_id):
    Rater_dict = {
        "raters": list(Rater.objects.filter(id=rater_id)),
        "ratings": list(Rating.objects.filter(user_id=rater_id))
    }

    return render(request, "Users.html", Rater_dict)