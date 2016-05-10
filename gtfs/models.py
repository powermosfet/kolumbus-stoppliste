from __future__ import unicode_literals

from django.db import models

class Stop(models.Model):
    stop_id   = models.CharField(max_length = 128, primary_key = True)
    stop_name = models.CharField(max_length = 128)
    stop_desc = models.CharField(max_length = 128)
    stop_lat  = models.FloatField()
    stop_lon  = models.FloatField()
    stop_url  = models.CharField(max_length = 128)

    def __unicode__(self):
        return "{}: {} ({})".format(self.stop_id, self.stop_name, self.stop_desc) \
            if self.stop_desc else \
           "{}: {}".format(self.stop_id, self.stop_name)
