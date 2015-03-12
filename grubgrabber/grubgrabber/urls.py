from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/add_profile/'

urlpatterns = patterns('',
    url(r'^$', 'grubgrabber.views.index',name='index'),
    url(r'^search/$', 'grubgrabber.views.search',name='search'),
    url(r'^search/getKey$', 'grubgrabber.views.getKey',name='getKey'),
    ## place page accessible through /place/?p=PLACE_ID
    url(r'^place/$', 'grubgrabber.views.place',name='place'),
    url(r'^profile$', 'grubgrabber.views.profile',name='profile'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

