from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views 

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return 'profile_registration'

urlpatterns = patterns('',
    url(r'^$', 'grubgrabber.views.index',name='index'),
    url(r'^search/$', 'grubgrabber.views.search',name='search'),
    url(r'^search/getKey$', 'grubgrabber.views.getKey',name='getKey'),
    ## place page accessible through /place/?p=PLACE_ID
    url(r'^place/(?P<SEARCH_LOC>.*)/(?P<PLACE_ID>.*)/$', 'grubgrabber.views.place',name='place'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^add_profile/$', 'grubgrabber.views.register_profile',name='register_profile'),
    url(r'^profile$', 'grubgrabber.views.profile',name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)
