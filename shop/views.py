from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.forms import ArticuloFormulario
from shop.models import Articulo, Cliente

from django.http import HttpResponse


def listar_articulos(request):
    contexto = {
        "articulos": Articulo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='shop/listado_articulos.html',
        context=contexto,
    )
    return http_response


def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            autor = data[autor]
            fecha = data["fecha"]
            creador = request.user
            articulo = Articulo(titulo=titulo, subtitulo=subtitulo, autor=autor, fehca=fecha, creador=creador)  # lo crean solo en RAM
            articulo.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('listar-articulos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ArticuloFormulario()
        
    http_response = render(
        request=request,
        template_name='shop/articulo_formulario.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulo = Articulo.objects.filter(titulo_contains=busqueda)
        contexto = {
            "articulo": articulo,
        }
        
        http_response = render(
            request=request,
            template_name='shop/listado_articulos.html',
            context=contexto,
        )
    return http_response


def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo.delete()
        url_exitosa = reverse('listar-articulos')
        return redirect(url_exitosa)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data['titulo']
            articulo.subtitulo = data['subtitulo']
            articulo.autor = data['autor']
            articulo.fecha = data['fecha']
            articulo.save()

            url_exitosa = reverse('listar-articulos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': articulo.titulo,
            'subtitulo': articulo.subtitulo,
            'autor': articulo.autor,
            'fecha': articulo.fecha,
        }
        formulario = ArticuloFormulario(initial=inicial)
    return render(
        request=request,
        template_name='shop/articulo_formulario.html',
        context={'formulario': formulario},
    )

class ClienteListView(LoginRequiredMixin, ListView):
     model = Cliente
     template_name = 'shop/listado_clientes.html'
     
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    success_url = reverse_lazy ('ver-clientes')
    
# Create your views here.
