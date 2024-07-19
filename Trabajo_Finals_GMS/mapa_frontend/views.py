from django.shortcuts import render

# Create your views here.

def barrioListaMapa(request):
    return render(request, 'mapa_frontend/Trabajo_Finals_GMS_base.html')