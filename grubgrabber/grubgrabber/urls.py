from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'grubgrabber.views.index',name='home'),
    url(r'^search/$', 'grubgrabber.views.search',name='home'),
    url(r'^place/(<PLACE_ID>.*)', 'grubgrabber.views.place',name='home'),
    url(r'^register$', 'grubgrabber.views.register',name='register'),
    url(r'^login$', 'grubgrabber.views.login',name='login'),
    url(r'^profile$', 'grubgrabber.views.profile',name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
