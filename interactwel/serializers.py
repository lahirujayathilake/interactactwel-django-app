from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Subbasin

class SubbasinSerializer(serializers.ModelSerializer):

    detail_json = serializers.JSONField()
    class Meta:
        model = Subbasin
        fields = ("id", "detail_json")