# Create your views here.
import json

from django.shortcuts import render, redirect
from .forms import FormularioGuitarra
from django.conf import settings

def leer_archivo(filename, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        usuarios=json.load(file)
    return usuarios


def actualizar_archivo(filename, form_data, settings):
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        usuarios=json.load(file)
    usuarios['guitarras'].append(form_data)
    with open(str(settings.BASE_DIR)+filename, 'w') as file:
        json.dump(usuarios, file)

def crear_usuario(request):
    formulario = FormularioGuitarra(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['Fecha_compra']=form_data['Fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/data/registro.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuarios=json.load(file)
        form_data['id'] = usuarios['ultimo_id_generado'] + 1
        usuarios['ultimo_id_generado'] = form_data['id']
        usuarios['registro'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(usuarios, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_usuario.html', context)

def crear_exitoso(request):
    filename= "/formularios/data/registro.json"
    usuarios = leer_archivo(filename, settings)
    return render(request, 'formularios/crear_exitoso.html', context=usuarios)



def eliminar_usuario(request, id):
    if request.method == "POST":
        filename= "/formularios/data/registro.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            usuarios=json.load(file)
        for usuarios in usuarios['registro']:
            print(int(usuarios['id']), int(id))
            if int(usuarios['id']) == int(id):
                usuarios['registro'].remove(usuarios)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(usuarios, file)
        return redirect('formularios:crear_exitoso')
    context = {'id': id} 
    return render(request, "formularios/eliminar_usuario.html", context)

def grafico2(request):
    lista = []
    lista_modelo = []
    filename= "/formularios/data/registro.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
        diccionario = guitarras.get('guitarras')
        for elemento in diccionario[-5:]:
            cuerdas = elemento.get('cuerdas')
            modelo = elemento.get('modelo')
            lista.append(cuerdas)
            lista_modelo.append(modelo)
    print(lista_modelo)
    context = {'modelo': lista_modelo, 'valor' : lista}
    return render(request, "formularios/grafico2.html", context)