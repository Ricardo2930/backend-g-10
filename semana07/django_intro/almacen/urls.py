from django.urls import path
from .views import renderHtml, buscarProducto
from .views import ProductosView, CategoriasView, ActualizarCategoriasView, OrdenesView

urlpatterns = [
    path('productos', renderHtml),
    path('producto/<int:producto_id>', buscarProducto),
    path('productos/listar', ProductosView.as_view()), #as_view es un metodo que sirve para indicar que la clase es una vista, sino se coloca lo toma como clase.
    path('categorias/listar/', CategoriasView.as_view()),
    path('categorias/actualizar/<int:categoria_id>', ActualizarCategoriasView.as_view()),
    path('ordenes/crear', OrdenesView.as_view())
]