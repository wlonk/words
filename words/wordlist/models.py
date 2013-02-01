from django.db import models
from django.core.urlresolvers import reverse


class Language(models.Model):
    iso = models.CharField(max_length=6, primary_key=True)

    class Meta:
        ordering = ('iso',)

    def __unicode__(self):
        return self.iso

    def get_absolute_url(self):
        return reverse('words', kwargs={'iso': self.iso, 'count': '1'})


class Word(models.Model):
    language = models.ForeignKey(Language)
    value = models.CharField(max_length=100)
    profane = models.BooleanField(default=False)

    class Meta:
        ordering = ('language', 'value',)
        unique_together = ('language', 'value')

    def __unicode__(self):
        return self.value
