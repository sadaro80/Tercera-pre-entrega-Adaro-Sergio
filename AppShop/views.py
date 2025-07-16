from django.shortcuts import render
from django.http import HttpResponse
from AppShop.models import *
from django.template import loader
from .forms import *


# Create your views here.
def inicio(request):
    return render(request, "AppShop/home.html")


def home(request):
    return render(request, "home.html")

def all_products(request):
    return render(request, "AppShop/all_products.html")

def kitchen(request):
    return render(request, "AppShop/kitchen.html")

def bedroom(request):
    return render(request, "AppShop/bedroom.html")

def bathroom(request):
    return render(request, "AppShop/bathroom.html")

def living_room(request):
    return render(request, "AppShop/living_room.html")




def contacto(request):  
    enviado = False
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            print(f"Mensaje recibido de {nombre} ({email}): {mensaje}")
            enviado = True
    else:
        form = ContactoForm()
    return render(request, "AppShop/contacto.html", {"form": form, "enviado": enviado})


def registrarse(request):
    registrado = False

    if request.method == "POST":
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            print("Cliente registrado:", datos)
            registrado = True
    else:
        form = ClienteRegistroForm()

    return render(request, "AppShop/registrarse.html", {"form": form, "registrado": registrado})



def iniciar_sesion(request):
    error = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # redirigí a la página principal
            else:
                error = "Usuario o contraseña incorrectos"
    else:
        form = LoginForm()

    return render(request, "AppShop/iniciar_sesion.html", {"form": form, "error": error})



