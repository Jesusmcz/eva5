from django.shortcuts import render

# Create your views here.

def inicio (request):
      return render (request, 'app/index.html')

def registro (request):
      return render (request, 'app/registro.html')

