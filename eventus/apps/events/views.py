#encoding:utf-8
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):

    template_name = 'events/home.html'