# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.contrib.gis.db import models

# Register your models here.
from .models import Piezometer, WebsiteText

class Media:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/acacia/js/tinymce_setup/tinymce_setup.js',
    ]

class WebsiteAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'htmleditor'})}}

admin.site.register(Piezometer)
admin.site.register(WebsiteText, WebsiteAdmin, Media = Media)