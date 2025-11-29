from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # --- RUTAS DE AUTENTICACIÓN ---
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro, name='registro'),

    # --- RUTAS DE VOLUNTARIOS ---
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('voluntarios/<int:pk>/', views.detalle_voluntario, name='detalle_voluntario'),
    path('voluntarios/crear/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntarios/editar/<int:pk>/', views.editar_voluntario, name='editar_voluntario'),
    path('voluntarios/eliminar/<int:pk>/', views.eliminar_voluntario, name='eliminar_voluntario'),

    # --- RUTAS DE EVENTOS ---
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:pk>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
]