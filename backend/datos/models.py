from django.db import models

# Create your models here.

class Loteo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Medidor(models.Model):
    medidor = models.CharField(max_length=20, primary_key=True, blank=True)
    cliente = models.CharField(max_length=100, default='', blank=True)
    fecha_instalacion = models.DateField(null=True, blank=True)
    lote = models.IntegerField(blank=True)
    manzana = models.IntegerField(blank=True)
    loteo_name = models.ForeignKey(Loteo, on_delete=models.CASCADE, related_name='medidor_loteo', default=1)
    lectura_anterior = models.IntegerField(default=0)
    lectura_actual = models.IntegerField(default=0)
    consumo = models.IntegerField(default=0)

    def __str__(self):
        return f"Medidor {self.medidor} de {self.dueño}"

    """ def save(self, *args, **kwargs):

        # Si la instancia ya existe en la base de datos
        if self.pk is not None:
            # Obtén la instancia actual desde la base de datos
            existing_medidor = Medidor.objects.get(pk=self.pk)
            # Actualiza lectura_anterior con el valor de lectura_actual de la base de datos
            self.lectura_anterior = existing_medidor.lectura_actual

        self.consumo = self.lectura_actual - self.lectura_anterior
        super(Medidor, self).save(*args, **kwargs) """