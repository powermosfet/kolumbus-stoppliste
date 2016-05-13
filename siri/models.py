from __future__ import unicode_literals

from django.db import models

class MonitoredVehicleJourney(models.Model):
    published_line_name = models.CharField(max_length = 8)
    destination_display = models.CharField(max_length = 128)
    expected_arrival = models.DateTimeField()
