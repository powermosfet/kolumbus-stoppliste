from django.conf.urls import include, url
from gtfs.views import stop_list, StopDetail

urlpatterns = [
    url(r'^stops/$', stop_list),
    url(r'^stops/(?P<pk>[0-9]+)/$', StopDetail.as_view()),
]
