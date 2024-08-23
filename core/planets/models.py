#model to define structure of the data
from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField(null=True, blank=True)
    terrains = models.CharField(max_length=255)
    climates = models.CharField(max_length=255)

    def __str__(self):
        return self.name