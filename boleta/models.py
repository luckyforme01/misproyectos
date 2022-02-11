from django.db import models
from django.utils import timezone

# Create your models here.

class Registro(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=timezone.now)
    sueldo_total = models.IntegerField()
    descuento = models.IntegerField()
    sueldo_bruto = models.IntegerField()
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    

