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
    lote = models.CharField(max_length=200, blank=True)
    manzana = models.CharField(max_length=200, blank=True)
    loteo_name = models.ForeignKey(Loteo, on_delete=models.CASCADE, related_name='medidor_loteo', default=1)
    lectura_anterior = models.IntegerField(null=True, blank=True)
    lectura_actual = models.IntegerField(null=True, blank=True)
    consumo = models.IntegerField(default=0)
    is_modificate = models.BooleanField(default=False)

    def __str__(self):
        return f"Medidor {self.medidor} de {self.dueño}"

    def save(self, *args, **kwargs):
        # Si la instancia ya existe en la base de datos
        if self.pk is not None:
            try:
                # Obtén la instancia actual desde la base de datos
                existing_medidor = Medidor.objects.get(pk=self.pk)
                # Actualiza lectura_anterior con el valor de lectura_actual de la base de datos
                self.lectura_anterior = existing_medidor.lectura_actual
                self.is_modificate = True
            except Medidor.DoesNotExist:
                # Si no existe, inicializa lectura_anterior a 0
                self.lectura_anterior = 0

        self.consumo = int(self.lectura_actual) - int(self.lectura_anterior)
        super(Medidor, self).save(*args, **kwargs)
        Medidor.reset_is_modificate()


    @classmethod
    def reset_is_modificate(cls):
        # Verifica si todos los medidores tienen is_modificate en True
        if cls.objects.filter(is_modificate=False).count() == 0:
            # Si todos tienen is_modificate en True, reinicializa a False
            cls.objects.all().update(is_modificate=False)