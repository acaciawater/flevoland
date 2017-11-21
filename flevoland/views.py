'''
Created on Oct 4, 2014

@author: theo
'''
from datetime import datetime
from pytz import utc

from django.shortcuts import get_object_or_404, render
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
    
    def determine_opacity(self, date):
        now = utc.localize(datetime.utcnow())
        seconds_ago = (now - date).total_seconds()
        if (seconds_ago > 86400.0):
            return 0.0
        else:
            return 0.5 + 0.5*(1.0 - seconds_ago/86400.0)
    
    def get_latest(self):
        meetlocatie = get_object_or_404(MeetLocatie,name='Perseel N')
        latest = [{
            'rectangle_id': x.rectangle_id,
            'value': x.series.laatste().value,
            'date': x.series.laatste().date,
            'opacity': self.determine_opacity(x.series.laatste().date),
            'url': reverse('acacia:series-detail', args=(x.series.pk, ))
            } for x in meetlocatie.piezometer_set.all()]
        return latest
    
    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['latest'] = self.get_latest()
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
    
def history_JS(request):
    meetlocatie = get_object_or_404(MeetLocatie,name='Perseel N')
    context = {'test': 'test'}
    return render(request, 'history.js', context)
