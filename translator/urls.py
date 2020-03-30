from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('alphabetModal/<str:pk>', views.alphabetModal, name="alphabetModal"),
]