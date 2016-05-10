from django.conf.urls import include, url
from gtfs.views import stop_list, StopDetail

urlpatterns = [
    url(r'^stops/$', stop_list),
    url(r'^stops/(?P<stop_id>[0-9]+)/$', StopDetail.as_view()),
]
