from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('listar/', views.listar_libros, name='listar_libros'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('modificar/<int:pk>/', views.modificar_libro, name='modificar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
