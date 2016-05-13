from django.conf.urls import include, url
from siri.views import siri as siri_view

urlpatterns = [
    url(r'^getstopmontoring/(?P<stop_id>[0-9]+)/$', siri_view),
]
