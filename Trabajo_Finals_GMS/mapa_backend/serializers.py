from .models import Barrio
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class barrioSerializador(GeoFeatureModelSerializer):
    class Meta:
        model = Barrio
        geo_field = 'geom'

        fields = (
            'id',
            'descripcion',
            'num_dist',
            'nombre'
        )

