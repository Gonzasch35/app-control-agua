from django.shortcuts import render
from django.http import HttpResponse
from .models import Medidor

# Create your views here.
def reset_medidores_view(request):
    Medidor.reset_all_is_modificate()
    return HttpResponse('Medidores reseteados!')