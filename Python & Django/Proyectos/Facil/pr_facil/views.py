from django.shortcuts import render
from django.http import HttpResponse

def fn_inicio(request):
    return render(request, 'pr_facil/inicio.html')

def fn_popayan(request):
    return render(request, 'pr_facil/popayan.html')