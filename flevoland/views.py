'''
Created on Oct 4, 2014

@author: theo
'''
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse

from acacia.data.models import Project, TabGroup, ProjectLocatie, MeetLocatie
from acacia.data.views import ProjectDetailView

class HomeView(ProjectDetailView):
    template_name = 'flevoland_detail.html'

    def get_object(self):
        return get_object_or_404(Project,name='flevoland')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['maptype'] = 'roadmap'
        return context
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

class LocationView(generic.DetailView):
    model = ProjectLocatie
    
    def get_latest_values(self):
        meetlocatie = get_object_or_404(MeetLocatie,name='Perseel N')
        latest_values =  [{'rectangle_id' : x.rectangle_id, 'level':x.series.laatste().value} for x in meetlocatie.piezometer_set.all()]
        return latest_values
    
    def get_urls(self):
        meetlocatie = get_object_or_404(MeetLocatie,name='Perseel N')
        urls = [{'rectangle_id' : x.rectangle_id, 'url':reverse('acacia:series-detail', args=(x.series.pk,))} for x in meetlocatie.piezometer_set.all()]
        return urls
    
    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['latest'] = self.get_latest_values()
        context['urls'] = self.get_urls()
        return context
    
    template_name = 'project_locatie_detail.html'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

class FirstDetailView(generic.DetailView):
    model = ProjectLocatie
    
    def get_context_data(self, **kwargs):
        context = super(FirstDetailView, self).get_context_data(**kwargs)
        return context
    
    template_name = 'details1.html'

class SecondDetailView(generic.DetailView):
    model = ProjectLocatie
    
    def get_context_data(self, **kwargs):
        context = super(SecondDetailView, self).get_context_data(**kwargs)
        return context
    
    template_name = 'details2.html'