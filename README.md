# pebble-sanntid-backend

bakcend api for [pebble sanntid](https://github.com/powermosfet/pebble-sanntid), a pebble app that shows realtime info about busses from Kolumbus

## Endpoints

* `kolumbus-stoppliste.herokuapp.com/api/gtfs/stops/`: complete list of stops
* `kolumbus-stoppliste.herokuapp.com/api/gtfs/stops/:id/`: a single stop
* `kolumbus-stoppliste.herokuapp.com/api/gtfs/stops/closest/:coords/`: lists the 5 stops closest to the given coordinates
