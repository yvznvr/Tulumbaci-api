from django.shortcuts import render
from rest_framework import viewsets
from .serializer import FireSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Fire


@csrf_exempt
def fire_list(request, id):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        if id != 'all':
            snippets = Fire.objects.filter(id=id)
        else:
            snippets = Fire.objects.all()
        serializer = FireSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FireSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class FireViewSet(viewsets.ModelViewSet):
    serializer_class = FireSerializer

    def get_object(self, queryset=None):
        return super().get_object()

    def get_queryset(self):
        return  Fire.objects.all()

    def perform_create(self, serializer):
        serializer.save()