from django.urls import path
from shop.views import index, comprar, devolver, listar_articulos, crear_articulo, buscar_articulo, eliminar_articulo, editar_articulo, \
ClienteListView, ClienteCreateView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView
from mysite.views import inicio, bienvenida, despedida, index, bienvenida_html, presentacion

urlpatterns = [
    
    path('inicio/', inicio, name="inicio"),
    path('', index),
    path('despedida/', despedida),
    path('hello/<str:cliente>', bienvenida),
    path('hello-html', bienvenida_html),
    path('compra/', comprar),
    path('devolucion/', devolver),
    path('listar-articulos/', listar_articulos, name="listar-articulo"),
    path('crear-articulos/', crear_articulo, name='crear-articulo'),
    path('buscar-articulos/', buscar_articulo, name='buscar-articulo'),
    path("eliminar-articulos/<int:id>/", eliminar_articulo, name="eliminar-articulo"),
    path("editar-articulos/<int:id>/", editar_articulo, name="editar-articulo"),
    path('clientes/', ClienteListView.as_view(), name="ver-clientes"),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name="ver-clientes"),
    path('crear-clientes/', ClienteCreateView.as_view(), name="crear-cliente"),
    path('editar-clientes/<int:pk>/', ClienteUpdateView.as_view(), name="editar-clientes"),
    path('borrar-clientes/<int:pk>/', ClienteDeleteView.as_view(), name="borrar-clientes"),
    path('presentacion/', presentacion, name="presentacion"),



]