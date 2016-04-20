from django.db import models

class Basin(models.Model):
    name = models.CharField('nome', max_length=200)
    area_km2 = models.FloatField('área (km²)')
    perimeter_km = models.FloatField('perímetro (km)')

    def __str__(self):
        return self.name
