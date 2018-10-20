from django.db import models
from django.utils import timezone


# Create your models here.
class Fire(models.Model):
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=4)
    confidence = models.FloatField()
    satalite = models.CharField(max_length=15, null=True, blank=True)
    daynight = models.CharField(max_length=1, null=True, blank=True)
    size = models.FloatField(default=0)
    direction = models.CharField(max_length=15, null=True, blank=True)
    flame_rate = models.FloatField(default=0, blank=True)
    smoke_rate = models.FloatField(default=0, blank=True)
    video = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.latitude + "-" + self.longitude
    
    class Meta:
        verbose_name = "Fire"


class Comment(models.Model):
    comment = models.TextField()
    fire = models.ForeignKey(Fire, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Comment"


class UpdateTime(models.Model):
    time = models.DateTimeField()