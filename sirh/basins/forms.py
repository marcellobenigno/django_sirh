from django.forms import ModelForm
from sirh.basins.models import Basin


class BasinForm(ModelForm):

    class Meta:
        model = Basin
        fields = ['name', 'area_km2', 'perimeter_km']