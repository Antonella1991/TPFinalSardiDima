from django.urls import path
from shop.views import listar_articulos, crear_articulo, buscar_articulo, eliminar_articulo, editar_articulo
from mysite.views import inicio, despedida, presentacion

urlpatterns = [
    
    path("", inicio, name="inicio"),
    path('despedida/', despedida),
    path('pages/', listar_articulos, name="listar-articulo"),
    path('crear-articulos/', crear_articulo, name='crear-articulo'),
    path('buscar-articulos/', buscar_articulo, name='buscar-articulo'),
    path("eliminar-articulos/<int:id>/", eliminar_articulo, name="eliminar-articulo"),
    path("editar-articulos/<int:id>/", editar_articulo, name="editar-articulo"),
    path('presentacion/', presentacion, name="presentacion"),



]