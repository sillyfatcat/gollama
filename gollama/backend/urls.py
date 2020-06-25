from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'shorthand', views.ShortHandViewSet)

urlpatterns = [
    path('', include(router.urls))
]
