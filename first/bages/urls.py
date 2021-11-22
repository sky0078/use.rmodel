from django.urls import path
from . import views

urlpatterns = [
    path('bages', views.index, name = "bages")

]