from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:shorthand>', views.reroute, name='index'),
    path('<str:shorthand>/<str:parameter>', views.reroute, name='index')
]