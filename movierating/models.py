from django.db import models

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1, null=True)
    occupation = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=12)
    video_release_date = models.CharField(max_length=12, default="")
    URL = models.CharField(max_length=300)
    unknown = models.IntegerField()
    Action = models.IntegerField()
    Adventure = models.IntegerField()
    Animation = models.IntegerField()
    Childrens = models.IntegerField()
    Comedy = models.IntegerField()
    Crime = models.IntegerField()
    Documentary = models.IntegerField()
    Drama = models.IntegerField()
    Fantasy = models.IntegerField()
    Film_Noir = models.IntegerField()
    Horror = models.IntegerField()
    Musical = models.IntegerField()
    Mystery = models.IntegerField()
    Romance = models.IntegerField()
    Sci_Fi = models.IntegerField()
    Thriller = models.IntegerField()
    War = models.IntegerField()
    Western = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    time_stamp = models.IntegerField()

    def __str__(self):
        return str(self.user_id)



