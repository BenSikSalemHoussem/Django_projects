from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default="9:00")
    duration = models.IntegerField(default=1)
