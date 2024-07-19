from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Barrio

barrio_mapping = {
    'id': 'id',
    'descripcion': 'descripcion',
    'num_dist': 'num_dist',
    'nombre': 'nombre',
    'geom': 'POINT',
}

barrio_gpkg = Path(__file__).resolve().parent / 'datos' / 'barrio.gpkg'

def run(verbose=True):
    lm = LayerMapping(Barrio, barrio_gpkg, barrio_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)