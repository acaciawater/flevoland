'''
Created on Oct 4, 2014

@author: theo
'''
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from acacia.data.models import Project, TabGroup
from acacia.data.views import ProjectDetailView
from acacia.data.models import Project, TabGroup
from acacia.data.views import ProjectDetailView

class HomeView(ProjectDetailView):
    template_name = 'flevoland_detail.html'

    def get_object(self):
        return get_object_or_404(Project,name='flevoland')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['maptype'] = 'SATELLITE'
        return context
