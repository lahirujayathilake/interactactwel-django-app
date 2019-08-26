from rest_framework import viewsets
from .models import Subbasin
from .serializers import SubbasinSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class SubbasinViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Subbasin.objects.all()
        serializer = SubbasinSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Subbasin.objects.all()
        subbasin = get_object_or_404(queryset, pk=pk)
        serializer = SubbasinSerializer(subbasin)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubbasinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subbasin created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)
