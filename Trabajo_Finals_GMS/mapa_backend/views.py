from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Barrio
from .serializers import barrioSerializador
from rest_framework import generics



class barrio(generics.ListAPIView):
    queryset = Barrio.objects.all()
    serializer_class = barrioSerializador
    name = 'barrio'