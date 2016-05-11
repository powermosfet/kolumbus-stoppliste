from django.http import HttpResponse
from gtfs.models import Stop
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import View
from geopy import distance
import json

def dictify(ob):
    r = { f.name: getattr(ob, f.name) for f in ob.__class__._meta.fields }
    r['api_url'] = '/api/gtfs/stops/{}'.format(ob.pk)
    if 'distance' in dir(ob):
        r['distance'] = int(ob.distance)
    return r

class JsonMixin(object):
    def get(self, *args, **kwargs):
        return HttpResponse(json.dumps(self.get_data(*args, **kwargs)), content_type = 'application/json')

class GetView(View):
    def dispatch(self, r, *args, **kwargs):
        if r.method != 'GET':
            return HttpResponse(status_code = 403)
        return super(GetView, self).dispatch(r, *args, **kwargs)

class StopDetail(GetView, SingleObjectMixin, JsonMixin):
    model = Stop

    def get_data(self, *args, **kwargs):
        return dictify(self.get_object())

class StopList(GetView, MultipleObjectMixin, JsonMixin):
    model = Stop

    def filter(self, stops):
        return stops

    def get_data(self, *args, **kwargs):
        return [ dictify(ob) for ob in self.filter(self.get_queryset()) ]

class ClosestStopList(StopList):
    def add_distance(self, stop):
        pos = tuple(self.kwargs['coords'].split(','))
        stop.distance = distance.great_circle(pos, (stop.stop_lat, stop.stop_lon)).m
        return stop
    
    def filter(self, stops):
        return sorted(map(self.add_distance, stops), key = lambda s: s.distance)[:5]
