from django import forms
from AppShop.models import Cliente
from AppShop.models import MensajeContacto
from AppShop.models import Producto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'rows': 2, 'cols': 50, 'class': 'form-control'}),
        }




class ClienteRegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ['usuario', 'nombre', 'apellido', 'email', 'telefono', 'ciudad', 'password']
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ClienteLoginForm(forms.Form):
    usuario = forms.CharField(label="Usuario", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'categoria', 'nombre', 'precio', 'descripcion', 'stock']
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 50, 'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),

        }

