from django.db import models

class Ruta(models.Model):
    MOVILIDAD_CHOICE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )

    movilidad_ruta_direccion = models.CharField(max_length=250)
    movilidad_ruta_hora_recojo = models.TimeField()
    movilidad_ruta_hora_retorno = models.TimeField()
    movilidad_id = models.IntegerField(choices=MOVILIDAD_CHOICE)

    #movilidad_id = models.ForeignKey(movilidad_id, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.movilidad_ruta_direccion
