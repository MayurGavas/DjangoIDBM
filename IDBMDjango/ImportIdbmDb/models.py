from django.db import models


class Person(models.Model):
    imdb_id = models.CharField(max_length=15, unique=True)
    person_name = models.CharField(max_length=255)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    primary_profession = models.TextField(null=True, blank=True)
    known_for_title = models.TextField(null=True, blank=True)

class Title(models.Model):
    tconst = models.CharField(max_length=15, primary_key=True)
    titleType = models.CharField(max_length=20)
    primaryTitle = models.TextField()
    originalTitle = models.TextField()
    isAdult = models.BooleanField()
    startYear = models.IntegerField(null=True)
    endYear = models.IntegerField(null=True)
    runtimeMinutes = models.IntegerField(null=True)
    genres = models.TextField(null=True)