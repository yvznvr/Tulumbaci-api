from django.db import models

# Create your models here.
class Fire(models.Model):
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    date = models.DateTimeField()
    time = models.CharField(max_length=4)
    confidence = models.FloatField()
    satalite = models.CharField(max_length=15)
    daynight = models.CharField(max_length=1, null=True, blank=True)
    size = models.FloatField(default=0)
    direction = models.CharField(max_length=15)
    flame_rate = models.FloatField(default=0)
    smoke_rate = models.FloatField(default=0)
    video = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.latitude + "-" + self.longitude
    
    class Meta:
        verbose_name = "Fire"
