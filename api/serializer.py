from rest_framework import serializers
from .models import Fire, Comment


class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire
        exclude = []


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []