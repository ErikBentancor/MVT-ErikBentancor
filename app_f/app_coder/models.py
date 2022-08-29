from django.db import models


class Familiar (models.Model):
    nombre = models.CharField(max_length=64)
    edad = models.IntegerField()
    cumpleaños = models.DateField()


    