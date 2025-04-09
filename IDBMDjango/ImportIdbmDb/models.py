from django.db import models


class Person(models.Model):
    imdb_id = models.CharField(max_length=15, unique=True)
    person_name = models.CharField(max_length=255)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    primary_profession = models.TextField(null=True, blank=True)
    known_for_title = models.TextField(null=True, blank=True)
