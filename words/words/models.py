from django.db import models


class Language(models.Model):
    iso = models.CharField(max_length=6, primary_key=True)


class Word(models.Model):
    language = models.ForeignKey(Language)
    value = models.CharField(max_length=100)
    profane = models.BooleanField(default=False)
