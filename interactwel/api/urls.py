from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'subbasins', views.SubbasinViewSet, basename='subbasin')

urlpatterns = [
    url(r'^', include(router.urls))
]