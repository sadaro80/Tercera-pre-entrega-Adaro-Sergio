from django.shortcuts import render
from django.http import HttpResponse
from AppShop.models import *
from django.template import loader
from AppShop.forms import ClienteRegistroForm
from AppShop.forms import ClienteLoginForm
from AppShop.forms import ContactoForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password




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
            form.save()
            enviado = True
            form = ContactoForm()  # limpiar el formulario
    else:
        form = ContactoForm()

    return render(request, "AppShop/contacto.html", {"form": form, "enviado": enviado})



def registrarse(request):
    registrado = False

    if request.method == "POST":
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.password = make_password(form.cleaned_data['password'])  # encriptar contraseña
            cliente.save()
            registrado = True
            form = ClienteRegistroForm()  # limpiar el formulario
    else:
        form = ClienteRegistroForm()

    return render(request, "AppShop/registrarse.html", {"form": form, "registrado": registrado})




  



def iniciar_sesion(request):
    error = None

    if request.method == "POST":
        form = ClienteLoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            try:
                cliente = Cliente.objects.get(usuario=usuario)
                if check_password(password, cliente.password):
                    return render(request, "AppShop/home.html", {"cliente": cliente})
                else:
                    error = "Contraseña incorrecta"
            except Cliente.DoesNotExist:
                error = "Usuario no encontrado"
    else:
        form = ClienteLoginForm()

    return render(request, "AppShop/iniciar_sesion.html", {"form": form, "error": error})




