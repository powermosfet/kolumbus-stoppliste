from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from gtfs.models import Stop

from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import View

def dictify(ob):
    return { f.name: getattr(ob, f.name) for f in ob.__class__._meta.fields }

class JsonMixin(object):
    def get(self, *args, **kwargs):
        return json.dumps(self.get_data())

class StopDetail(View, SingleObjectMixin, JsonMixin):
    def get_data(self):
        return dictify(self.get_object())

def stop_list(r):
    s = FlatJsonSerializer()
    return HttpResponse(s.serialize("json", Stop.objects.all()))

def stop_detail(r, stop_id):
    s = FlatJsonSerializer()
    try:
        stop_ob = Stop.objects.get(pk = stop_id)
    except ObjectDoesNotExist:
        return HttpResponse("The stop could not be found", status_code = 404)
    return HttpResponse(s.serialize("json", stop_ob))
