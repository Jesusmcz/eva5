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
    Genero = forms.IntegerField(initial=6,
                    validators=[validators.MinValueValidator(6, "Mínimo 6 cuerdas!!"),
                                validators.MaxValueValidator(12, "Máximo 12 cuerdas!!")])
    fecha_compra = forms.DateField( validators=[validar_fecha])

