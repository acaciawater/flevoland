# -*- coding: utf-8 -*-
from django.db import models
from acacia.data.models import Series, MeetLocatie

class Piezometer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='omschrijving')
    meetlocatie = models.ForeignKey(MeetLocatie)
    series = models.ForeignKey(Series, verbose_name='reeks')
    rectangle_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='rectangle ID', help_text='ID van de bijbehorende SVG rectangle')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'piezometers'
        
class WebsiteText(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contents = models.TextField(blank=True, null=True)