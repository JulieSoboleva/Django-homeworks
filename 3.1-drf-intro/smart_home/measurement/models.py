from django.db import models


class Sensor(models.Model):
    name = models.CharField()
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,
                               related_name='measurements')
    photo = models.ImageField(upload_to='Images/',
                              blank=True, null=True)
