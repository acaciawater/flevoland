import json, pytz
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings

from acacia.data.models import Project, TabGroup, ProjectLocatie, MeetLocatie, Series
from .models import WebsiteText
from acacia.data.views import ProjectDetailView
from django.utils.formats import localize
from django.views.decorators.cache import cache_page



class HomeView(ProjectDetailView):
    template_name = 'flevoland_detail.html'

    def get_object(self):
        return get_object_or_404(Project,name='Spaarwater Flevoland')

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
    template_name = 'locatie.html'
    
    def get_urls(self):
        meetlocatie = get_object_or_404(MeetLocatie, name='Perseel N')
        urls = [{
            'rectangle_id': x.rectangle_id,
            'url': reverse('acacia:series-detail', args=(x.series.pk, ))
            } for x in meetlocatie.piezometer_set.all()]
        return urls
    
    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        now = pytz.utc.localize(datetime.utcnow())
        context['neerslag'] = get_object_or_404(Series, name='Precipitation P5 (ECRN-100)')
        context['data'] = get_data(now)
        context['urls'] = self.get_urls()
        return context


class FirstDetailView(generic.DetailView):
    model = ProjectLocatie
    template_name = 'details1.html'
    
    def get_pks(self):
        meetlocatie = get_object_or_404(MeetLocatie, name='Perseel N')
        pks = [{
            'id': x.rectangle_id,
            'pk': x.series.pk,
            'name': x.name
            } for x in meetlocatie.piezometer_set.all()]
        return pks
    
    def get_context_data(self, **kwargs):
        context = super(FirstDetailView, self).get_context_data(**kwargs)
        now = pytz.utc.localize(datetime.utcnow())
        context['neerslag'] = get_object_or_404(Series, name='Precipitation P5 (ECRN-100)')
        context['data'] = get_data(now)
        context['pks'] = self.get_pks()
        return context
    


class SecondDetailView(generic.DetailView):
    model = ProjectLocatie
    template_name = 'details2.html'
    
    def get_context_data(self, **kwargs):
        context = super(SecondDetailView, self).get_context_data(**kwargs)
        return context
    
    
    
def info(request):
    context = {'info':WebsiteText.objects.get(name='Algemene Informatie').contents}
    return render(request,'info.html',context=context)


@cache_page(60 * 60 * 6)
def history_JS(request):
    date = request.GET.get('date')
    timezone = pytz.timezone(settings.TIME_ZONE)
    day = timezone.localize(datetime.strptime(date,'%Y-%m-%d'))
    day = day + timedelta(hours = 12)
    j = json.dumps({'date':date, 'values':get_data(day)})
    return HttpResponse(j, content_type='application/json')
