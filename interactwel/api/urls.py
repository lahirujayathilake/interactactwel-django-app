from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'subbasins', views.SubbasinViewSet, base_name='subbasin')

urlpatterns = [
    url(r'^', include(router.urls))
]