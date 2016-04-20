from django.db import models
from sirh.basins.models import Basin

class River(models.Model):
    name = models.CharField('nome', max_length=200)
    order = models.IntegerField('ordem')
    length_km = models.FloatField('área (km²)')
    basin = models.ForeignKey(Basin, verbose_name="bacia hidrográfica")


    def __str__(self):
        return self.name