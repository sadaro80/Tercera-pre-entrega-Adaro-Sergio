from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('Home', views.home, name = 'home'),
    path('all_products', views.all_products, name = 'all_products'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('bedroom/', views.bedroom, name='bedroom'),
    path('bathroom/', views.bathroom, name = 'bathroom'),
    path('living_room/', views.living_room, name = 'living_room'),
    path('contacto/', views.contacto, name= 'contacto'),
    path('registrarse/', views.registrarse, name= 'registrarse'),
    path('iniciar_sesion/', views.iniciar_sesion, name= 'iniciar_sesion') 

]