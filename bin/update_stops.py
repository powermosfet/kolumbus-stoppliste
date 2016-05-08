import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stoppliste.settings")
django.setup()

import io, requests, zipfile
from contextlib import closing

from gtfs.models import Stop
from django.core.exceptions import ObjectDoesNotExist

url = "http://www.rkt.no/gt/google_transit.zip"

print "Fetching new stop list from", url
r = requests.get(url)
if r.status_code == 200:
    print "File downloaded. Processing..."
    new, changed = 0 ,0
    with closing(r), zipfile.ZipFile(io.BytesIO(r.content)) as archive:
        stops = archive.open('stops.txt')
        iterstops = iter(stops)
        next(iterstops)
        for s in iterstops:
            stop_id,stop_name,stop_desc,stop_lat,stop_lon,stop_url = s.split(",")
            try: 
                stop = Stop.objects.get(pk = int(stop_id))
            except ObjectDoesNotExist:
                stop = Stop()
                new += 1
            else:
                changed += 1
            stop.stop_id   = int(stop_id)
            stop.stop_name = stop_name
            stop.stop_desc = stop_desc
            stop.stop_lat  = float(stop_lat)
            stop.stop_lon  = float(stop_lon)
            stop.stop_url  = stop_url            
            stop.save()
    print "Done processing file.", new, "new,", changed, "changed."
else:
    print "Error fetching file:", r.status_code
