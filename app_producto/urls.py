from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_producto, name='add'),
    path('edit/<int:id_producto>/', views.edit_producto, name='edit'),
    path('delete/<int:id_producto>/', views.delete_producto, name='delete'),
]
