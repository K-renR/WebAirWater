from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signIn/', views.signIn, name='signIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('signOut/', views.signOut, name='signOut'),
    path('adminPanel/', views.adminPanel, name='adminPanel'),
    path('gestionComunidad/', views.gestionComunidad, name='gestionComunidad'),
    path('gestionUsuarios/', views.gestionUsuarios, name='gestionUsuarios'),
    path('registrarComunidad/', views.registrarComunidad, name='registrarComunidad'),
    path('registrarUsuarios/', views.registrarUsuarios, name='registrarUsuarios'),
    path('gestionComunidad/editarComunidad/<codigo>', views.editarComunidad),
    path('gestionUsuarios/editarUsuario/<codigo>', views.editarUsuarios),
    path('edicionComunidad/', views.edicionComunidad),
    path('edicionUsuarios/', views.edicionUsuarios),
    path('gestionComunidad/eliminarComunidad/<codigo>', views.eliminarComunidad, name='eliminarComunidad'),
    path('gestionUsuarios/eliminarUsuarios/<codigo>', views.eliminarUsuarios, name='eliminarUsuarios')
]