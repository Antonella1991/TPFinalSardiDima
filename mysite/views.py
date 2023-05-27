from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {}
    
    http_response = render(
        request=request,
        template_name='shop/index.html',
        context=contexto,
    )
    return http_response

def despedida(request):
    contexto = {}
    
    http_response = render(
        request=request,
        template_name='shop/base.html',
        context=contexto,
    )
    return http_response

def presentacion(request):
    contexto = {}
    
    http_response = render(
        request=request,
        template_name='shop/presentacion.html',
        context=contexto,
    )
    return http_response