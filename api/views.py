from django.shortcuts import render
from rest_framework import viewsets
from .serializer import FireSerializer, CommentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Fire, Comment, UpdateTime


class FireViewSet(viewsets.ModelViewSet):
    serializer_class = FireSerializer

    def get_object(self, queryset=None):
        return super().get_object()

    def get_queryset(self):
        return  Fire.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_object(self, queryset=None):
        return super().get_object()

    def get_queryset(self):
        return  Comment.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

from dbfread import DBF
import json
from django.utils import timezone
from os import system
from time import sleep

def get_nasa_data(request):
    file = "/tmp/nasa/MODIS_C6_Global_24h.dbf"
    url = "https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_Global_24h.zip"
    first = UpdateTime.objects.first()
    time = first.time
    time = timezone.now() - time
    if time.total_seconds()>600: #1800 means 30 minutes
        try:
            system("rm -r /tmp/nasa/")
            system("rm -r /tmp/data.zip")
        except:
            pass
        system("curl {0} --output /tmp/data.zip".format(url))
        system("unzip /tmp/data.zip -d /tmp/nasa")
        first.time = timezone.now()
        first.save()
    data = []
    for record in DBF(file):
        record['ACQ_DATE'] = str(record['ACQ_DATE'])
        data.append(record)
    return HttpResponse(json.dumps(data), content_type="application/json")
