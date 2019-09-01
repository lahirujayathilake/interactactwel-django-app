from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework import routers

from . import views

app_name = "interactwel"

router = routers.DefaultRouter()
router.register(r"subbasins", views.SubbasinViewSet, base_name="subbasin")

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(
        "",
        TemplateView.as_view(template_name="interactwel/application.html"),
        name="app",
    ),
]
