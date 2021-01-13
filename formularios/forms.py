import datetime

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2020-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo fechas de diciembre 2020")


class FormularioGuitarra(forms.Form):
    Nombre = forms.CharField(initial="Fender",
                    validators=[validators.MinLengthValidator(4, "Mínimo 4 letras")])
    Apellido = forms.CharField( )
    Edad = forms.IntegerField(
                    validators=[validators.MinValueValidator(18, "Mínimo 18 años!!"),
                                validators.MaxValueValidator(120, "Máximo 120 años!!")])
    Fecha_compra = forms.DateField( validators=[validar_fecha])

