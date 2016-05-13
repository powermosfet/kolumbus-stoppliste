from datetime import datetime
from django.http import HttpResponse
from suds import WebFault
from suds.client import Client
import config, json

def dictify(d, v):
    r = {
            'expected_departure_time': getattr(v.MonitoredVehicleJourney.MonitoredCall, 'ExpectedDepartureTime', None),
            'aimed_departure_time': getattr(v.MonitoredVehicleJourney.MonitoredCall, 'AimedDepartureTime', None),
            'published_line_name': v.MonitoredVehicleJourney.PublishedLineName,
            'destination_display': v.MonitoredVehicleJourney.MonitoredCall.DestinationDisplay,
            'departure_status': getattr(v.MonitoredVehicleJourney.MonitoredCall, 'DepartureStatus', 'unknown'),
        }
    if r['expected_departure_time']:
        r['expected_departure_time'] = r['expected_departure_time'].isoformat()
    if r['aimed_departure_time']:
        r['aimed_departure_time'] = r['aimed_departure_time'].isoformat()
    return r

def siri(r, *args, **kwargs):
    c = Client(config.url)
    info = c.factory.create('ns5:ServiceRequestInfo')
    request = c.factory.create('ns5:StopMonitoringRequest')
    info.RequestTimestamp = r.GET.get('timestamp', datetime.now())
    info.RequestorRef = '1234'
    request.MonitoringRef = r.GET.get('stop_id', '')
    request.RequestTimestamp = r.GET.get('timestamp', datetime.now())
    request._version = '1.4'
    try:
        result = c.service.GetStopMonitoring(info, request)
    except WebFault:
        return HttpResponse(status = 500)
    if result.Answer.StopMonitoringDelivery:
        print result.Answer
        json_data = json.dumps([ dictify(d, v)
            for d in result.Answer.StopMonitoringDelivery
            for v in getattr(d, 'MonitoredStopVisit', [])
        ])
        return HttpResponse(json_data, content_type = 'application/json')
