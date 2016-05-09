from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from gtfs.models import Stop

def stop_list(r):
    return HttpResponse(serializers.serialize("xml", Stop.objects.all()))

def stop_detail(r, stop_id):
    try:
        stop_ob = Stop.objects.get(pk = stop_id)
    except ObjectDoesNotExist:
        return HttpResponse("The stop could not be found", status_code = 404)
    return HttpResponse(serializers.serialize("xml", stop_ob))
