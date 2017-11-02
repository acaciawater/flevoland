'''
Created on Oct 4, 2014

@author: theo
'''
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views import generic

from acacia.data.models import Project, TabGroup, ProjectLocatie
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
    
    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['test'] = 'test'
        return context
    
    template_name = 'project_locatie_detail.html'

class FirstDetailView(generic.DetailView):
    model = ProjectLocatie
    
    def get_context_data(self, **kwargs):
        context = super(FirstDetailView, self).get_context_data(**kwargs)
        context['test'] = 'test'
        return context
    
    template_name = 'details1.html'

class SecondDetailView(generic.DetailView):
    model = ProjectLocatie
    
    def get_context_data(self, **kwargs):
        context = super(SecondDetailView, self).get_context_data(**kwargs)
        context['test'] = 'test'
        return context
    
    template_name = 'details2.html'