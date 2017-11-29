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
        
        
class SVGMetadata(models.Model):
    meetlocatie = models.OneToOneField(MeetLocatie, related_name='SVG_metadata')
    svg_file_name = models.CharField(max_length=50)
    rectangle1_id = models.CharField(max_length=50)
    rectangle2_id = models.CharField(max_length=50)
    precipitation_per_day = models.ForeignKey(Series)
    precipitation_per_hour = models.ForeignKey(Series, related_name='SVG_Metadata_set')
        
class WebsiteText(models.Model):
    name = models.CharField(max_length=50)
    meetlocatie = models.ForeignKey(MeetLocatie, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['name',]
        unique_together = ('meetlocatie', 'name', )