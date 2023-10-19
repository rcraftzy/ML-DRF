from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import numpy as np
import pandas as pd
import tensorflow as tf
tf.__version__

# Create your views here.
class RNATrainnigView(APIView):
    def get(self, request, *args, **kwargs):
        # PreProcesamiento de datos
        
        return Response({'data': 'serializer.data'}, status = status.HTTP_200_OK)
