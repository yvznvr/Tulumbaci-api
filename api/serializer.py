from rest_framework import serializers
from .models import Fire


class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire
        exclude = []
