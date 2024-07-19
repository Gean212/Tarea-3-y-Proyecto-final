from django.contrib.gis import admin
from .models import Barrio


# Register your models here.
class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 12,
            'default_lon': -84.832955,
            'default_lat': 9.977484,
        }
    }
    

@admin.register(Barrio)
class BarrioAdmin(CustomGeoAdmin):
    pass