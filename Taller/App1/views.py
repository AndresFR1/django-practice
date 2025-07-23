from django.shortcuts import render
from django.http import HttpResponse
from .models import AutorDb, Frasedb

# Create your views here.
def IndexView(request):

    objecto = AutorDb.objects.all() 

    return render(request, 'index.html', {'objecto': objecto})
