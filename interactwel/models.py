from rest_framework import serializers
from django.db import models
from jsonfield import JSONField

class Subbasin(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    detail_json = JSONField()

    class Meta:
        managed = True
        db_table = 'subbasin'
        verbose_name = 'Subbasin'
        verbose_name_plural = 'Subbasins'
