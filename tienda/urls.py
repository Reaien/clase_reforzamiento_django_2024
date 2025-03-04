from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('agregar-producto', views.agregar_producto, name='agregar_producto'),
    path('listar-producto', views.listar_producto, name='listar_producto'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
]
