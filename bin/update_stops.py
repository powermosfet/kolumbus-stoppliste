import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pebble_sanntid_backend.settings")
django.setup()

import io, requests, zipfile
from contextlib import closing
from itertools import izip
from gtfs.models import Stop
from django.core.exceptions import ObjectDoesNotExist

url = "http://www.rkt.no/gt/google_transit.zip"

print "Fetching new stop list from", url
r = requests.get(url)
if r.status_code == 200:
    print "File downloaded. Processing..."
    new, changed, skipped = 0 ,0, 0
    with closing(r), zipfile.ZipFile(io.BytesIO(r.content)) as archive:
        stops = archive.open('stops.txt')
        iterstops = iter(stops.readlines())
        header = next(iterstops)
        fieldnames = header.strip().split(',')
        converters = {
            'stop_lat': lambda x: float(x),
            'stop_lon': lambda x: float(x),
            }
        for s in iterstops:
            stopdict = {}
            values = s.strip().split(',')
            for (fieldname, value) in izip(fieldnames, values):
                if fieldname in converters:
                    stopdict[fieldname] = converters[fieldname](value)
                else:
                    stopdict[fieldname] = value
            try: 
                stop = Stop.objects.get(pk = stopdict['stop_id'])
            except ObjectDoesNotExist:
                stop = Stop()
                new += 1
            else:
                changed += 1
            for k in stopdict:
                setattr(stop, k, stopdict[k])
            stop.save()
    print "Done processing file.", new, "new,", changed, "changed,", skipped, "skipped."
else:
    print "Error fetching file:", r.status_code
