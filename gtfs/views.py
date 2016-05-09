from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from gtfs.models import Stop
from serializers.flatjsonserializer import FlatJsonSerializer

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
