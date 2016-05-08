import io, requests, zipfile
from contextlib import closing
from gtfs.models import Stop

url = "http://www.rkt.no/gt/google_transit.zip"

print "Fetching new stop list from", url
r = requests.get(url)
if r.statuscode == 200:
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
            except DoesNotExist:
                stop = Stop()
                new += 1
            else:
                changed += 1
            s.stop_id   = int(stop_id)
            s.stop_name = stop_name
            s.stop_desc = stop_desc
            s.stop_lat  = float(stop_lat)
            s.stop_lon  = float(stop_lon)
            s.stop_url  = stop_url            
            s.save()
    print "Done processing file.", new, "new,", changed, "changed."
else:
    print "Error fetching file:", r.statuscode
