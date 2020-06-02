from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('<str:shorthand>', views.redirect, name='index')
]