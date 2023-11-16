from django.http import HttpResponse
from django.shortcuts import render
def saludo(request):
    return HttpResponse("Hola Django - Coder ")

def saludo_html(request):
    return HttpResponse("<b>Hola Django</b> - Coder ")

def saludo_nombre(request,nombre):
    return HttpResponse(f"<h1>{nombre}</h1><br><b>Hola Django</b>")

def saludo_plantilla(request):
    # Logica del negocio
    contexto = {
        "nombre": "Andres",
        "edad": 30,
        "hijos":[
            {
                "nombre": "hijo1",
                "edad": 1
            },
            {
                "nombre": "hijo1",
                "edad": 1
            },


        ]
    }
    return render(request, "index.html", contexto)


