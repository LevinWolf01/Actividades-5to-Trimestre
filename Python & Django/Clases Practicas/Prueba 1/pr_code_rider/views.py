from django.shortcuts import render

def fn_inicio(request):
    return render(request, 'pr_code_rider/bienvenida.html')