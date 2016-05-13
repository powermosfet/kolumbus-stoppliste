from datetime import datetime
from django.shortcuts import render
from suds import WebError
from suds.client import Client
import config

def siri(request, *args, **kwargs):
    c = Client(config.url)
    info = c.factory.create('ns5:ServiceRequestInfo')
    request = c.factory.create('ns5:StopMonitoringRequest')
    info.RequestTimestamp = datetime.now()
    info.RequestorRef = '1234'
    request.MonitoringRef = kwargs.get('stop_id', '')
    request.RequestTimestamp = datetime.now()
    request._version = '1.4'
    result = c.GetStopMonitoring(info, request)
    if result.Answer.StopMonitoringDelivery:
        json_data = json.dumps([
            {
                'expected_departure_time': v.MonitoredVehicleJourney.MonitoredCall.ExpectedDepartureTime,
                'published_line_name': v.MonitoredVehicleJourney.PublishedLineName,
                'destination_display': v.MonitoredVehicleJourney.MonitoredCall.DestinationDisplay,
                'departure_status': v.MonitoredVehicleJourney.MonitoredCall.DepartureStatus,
            }
            for d in result.Answer.StopMonitoringDelivery
            for v in d.MonitoredStopVisit
        ])
        return HttpResponse(json_data, content_type = 'application/json')
