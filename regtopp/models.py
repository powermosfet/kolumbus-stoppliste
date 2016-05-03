from django.db import models

class Stop(models.Model):
    admin_code = models.IntegerField()
    seqnr = models.IntegerField()
    stop_nr = models.IntegerField()
    full_name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=5)
    zone = models.CharField(max_length=6)
    x = models.IntegerField()
    y = models.IntegerField()
    zone_nr_1 = models.IntegerField()
    zone_nr_2 = models.IntegerField()
    stop_type = models.IntegerField()
    reboard_time = models.IntegerField()
    stop_class = models.IntegerField()
