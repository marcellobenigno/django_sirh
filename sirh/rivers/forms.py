from django.forms import ModelForm
from sirh.rivers.models import River


class RiverForm(ModelForm):

    class Meta:
        model = River
        fields = ['name', 'order', 'length_km', 'basin']