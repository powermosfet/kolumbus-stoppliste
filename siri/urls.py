from django.conf.urls import include, url
from siri.views import siri as siri_view

urlpatterns = [
    url(r'^getstopmonitoring/$', siri_view),
]
