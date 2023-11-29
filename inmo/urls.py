from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    ############### MAIN ###############
    path('', views.home),
    path('propiedades',views.propiedades),
    path('fC/<propiedad_id>',views.fC),
    path('compra/',views.compra),
    ############### CUENTA USUARIO ###############
    path('mi_cuenta/inicio',views.mi_cuenta),
    path('mi_cuenta/propiedades',views.propiedadesUsuario),
    path('mi_cuenta/configurar',views.mi_configuracion),
    path('propiedad/<propiedad_id>',views.propiedad),
    path('registro/',views.registro),
    path('login/', LoginView.as_view(template_name ='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name ='logout.html'), name='logout'),
    ############### PANEL DE ADMIN ###############
    path('panel_admin/inicio', views.paneladmin),
    path('panel_admin/usuarios', views.lst_usr),
    ############### CONTACTO ###############
    path('panel_admin/contactado/<compra_id>', views.contactado),
    ############### PROPIEDADES ###############
    path('panel_admin/propiedades', views.lst_p),
    path('panel_admin/eliminarPropiedad/<propiedad_id>',views.eliminarPropiedad),
    path('panel_admin/crearP', views.crearP),
    path('panel_admin/edicionPropiedad/<propiedad_id>', views.edicionPropiedad),
    path('panel_admin/editarPropiedad/', views.editarP),
    path('panel_admin/registrar_propiedad/', views.registrar_propiedad),
    ############### COMUNAS ###############
    path('panel_admin/comunas', views.lst_c),
    path('panel_admin/crearC', views.crearC),
    path('panel_admin/registrar_comuna/', views.registrar_comuna),
    path('panel_admin/edicionComuna/<comuna_id>', views.edicionComuna),
    path('panel_admin/eliminarComuna/<comuna_id>',views.eliminarComuna),
    path('panel_admin/editarComuna/', views.editarC),

]