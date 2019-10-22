from django.db import models
from django_countries import fields
from languages.fields import LanguageField

# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.other_name

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.other_name

class Writer(models.Model):
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name+" "+self.other_name

class Rating(models.Model):
    rating = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.rating

class Awards(models.Model):
    award = models.CharField(max_length=50)
    def __str__(self):
        return self.award

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.genre


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    year = models.IntegerField()
    image = models.CharField(max_length=250)
    rated = models.ForeignKey(Rating,on_delete=models.CASCADE)
    country = fields.CountryField()
    language = LanguageField()
    plot = models.CharField(max_length=250, default="Any Plot, We shall add here later")
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE,null=True,blank=True)
    awards = models.ManyToManyField(Awards,related_name='awards',blank=True)
    runtime = models.IntegerField()

    def __str__(self):
        return self.title