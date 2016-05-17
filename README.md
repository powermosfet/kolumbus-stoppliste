# pebble-sanntid-backend

bakcend api for [pebble sanntid](https://github.com/powermosfet/pebble-sanntid), a pebble app that shows realtime info about busses from Kolumbus

## Endpoints

* `pebble-sanntid-backend.herokuapp.com/api/gtfs/stops/`: complete list of stops
* `pebble-sanntid-backend.herokuapp.com/api/gtfs/stops/<id>/`: a single stop
* `pebble-sanntid-backend.herokuapp.com/api/gtfs/stops/closest/?coords=<coords>`: lists the 5 stops closest to the given coordinates
* `pebble-sanntid-backend.herokuapp.com/api/siri/getstopmonitoring/?stop_id=<stop_id>&timestamp=<timestamp>`: get realtime data for a stop
