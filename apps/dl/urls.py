from django.urls import path

from .views import *

urlpatterns = [
    path('rna_training', RNATrainnigView.as_view())
]
