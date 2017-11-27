'''
Created on Oct 4, 2014

@author: theo
'''
import json, pytz
from datetime import datetime, timedelta
from pytz import utc

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings

from acacia.data.models import Project, TabGroup, ProjectLocatie, MeetLocatie, Series
from acacia.data.views import ProjectDetailView
from django.utils.formats import localize
from django.views.decorators.cache import cache_page



class HomeView(ProjectDetailView):
    template_name = 'flevoland_detail.html'

    def get_object(self):
        return get_object_or_404(Project,name='flevoland')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['maptype'] = 'roadmap'
        return context
    

def determine_opacity(date, comparison_date):
    difference_in_seconds = abs((comparison_date - date).total_seconds())
    if (difference_in_seconds > 86400.0):
        return 0.0
    else:
        return 0.5 + 0.5*(1.0 - difference_in_seconds/86400.0)    
    
    
def get_data(day):
    meetlocatie = get_object_or_404(MeetLocatie,name='Perseel N')
    data_list = []
    timezone = pytz.timezone(settings.TIME_ZONE)
    for x in meetlocatie.piezometer_set.all():
        datapoint = x.series.datapoints.filter(date__lte=day).latest('date')
        if datapoint is None:
            datapoint = x.series.datapoints.all().earliest('date')
            
        data_list.append({
            'id': x.rectangle_id,
            'val': datapoint.value,
            'date': localize(datapoint.date.astimezone(timezone)),
            'op': determine_opacity(datapoint.date, day)
            })
    return data_list


class LocationView(generic.DetailView):
    model = ProjectLocatie
    
    def get_urls(self):
        meetlocatie = get_object_or_404(MeetLocatie, name='Perseel N')
        urls = [{
            'rectangle_id': x.rectangle_id,
            'url': reverse('acacia:series-detail', args=(x.series.pk, ))
            } for x in meetlocatie.piezometer_set.all()]
        return urls
    
    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        now = utc.localize(datetime.utcnow())
        context['neerslag'] = get_object_or_404(Series, name='Precipitation P5 (ECRN-100)')
        context['data'] = get_data(now)
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
    
    
    
    
    
    
    
    
    
    

@cache_page(60 * 60 * 24)
def history_JS(request):
    date = request.GET.get('date')
    timezone = pytz.timezone(settings.TIME_ZONE)
    day = timezone.localize(datetime.strptime(date,'%Y-%m-%d'))
    day = day + timedelta(hours = 12)
    j = json.dumps({'date':date, 'values':get_data(day)})
    return HttpResponse(j, content_type='application/json')
