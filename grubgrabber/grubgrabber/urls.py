from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views
from django.conf import settings

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return 'register_profile'

urlpatterns = patterns('',
    url(r'^$', 'grubgrabber.views.index',name='index'),
    url(r'^search/$', 'grubgrabber.views.search',name='search'),
    url(r'^search/getKey$', 'grubgrabber.views.getKey',name='getKey'),
    ## place page accessible through /place/USER_LOCATION/PLACE_ID
    url(r'^place/(?P<SEARCH_LOC>.*)/(?P<PLACE_ID>.*)/$', 'grubgrabber.views.place',name='place'),
    url(r'^place/(?P<PLACE_ID>.*)/$', 'grubgrabber.views.placeNoLoc', name='placeNoLoc'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^add_profile/$', 'grubgrabber.views.register_profile',name='register_profile'),
    url(r'^profile/$', 'grubgrabber.views.profile',name='profile'),
    url(r'^add_favourite/$', 'grubgrabber.views.addFavourite', name='addFavourite'),
    url(r'^add_blacklist/$', 'grubgrabber.views.addBlacklist', name='addBlacklist'),
    url(r'^add_like/$', 'grubgrabber.views.addLike', name='addLike'),
    url(r'^sort_results/$', 'grubgrabber.views.sort_search_results', name='sortResults'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
