from django import forms 
from .models import Monitores, Amplificadores, Notebooks
from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm, PasswordChangeForm

class MonitoresForm(forms.ModelForm):
    class Meta:
        model = Monitores
        fields=['nombre', 'precio','cantidad', 'tamaño', 'imagen', 'descripcion', 'user']
        widgets={
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'user.id', 'type':'hidden'})
        }
        

class AmplificadoresForm(forms.ModelForm):
    class Meta:
        model = Amplificadores
        fields=['nombre', 'precio','cantidad', 'potencia', 'imagen', 'descripcion', 'user']
        widgets={
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'user.id', 'type':'hidden'})
        }
        

class NotebooksForm(forms.ModelForm):
    class Meta:
        model = Notebooks
        fields=['nombre', 'precio','cantidad','imagen','descripcion', 'user']
        widgets={
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'user.id', 'type':'hidden'})
        }
        
        
class UsuariosForm(UserCreationForm):
    username= forms.TextInput()
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields=['username','email', 'password1', 'password2']
        help_texts={k:"" for k in fields}
        

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name' ]
        
class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña actual"), widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=("Nueva contraseña"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("Repita nueva contraseña"), widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ['old_password', 'new_password1', 'new_password2']