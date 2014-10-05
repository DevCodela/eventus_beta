from django.conf.urls import patterns, include, url

from .views import HomeTemplateView

urlpatterns = patterns('',

    url(r'^$', HomeTemplateView.as_view(), name='home'),

)
