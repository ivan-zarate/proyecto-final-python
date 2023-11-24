from django.shortcuts import render, redirect
from .models import Notebooks, Amplificadores, Monitores
from .forms import AmplificadoresForm, NotebooksForm, MonitoresForm, UsuariosForm, UserEditForm, PasswordEditForm
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
    
    
def inicio(req):
    result=req.GET.get("Buscar")
    if result:
        notebooks=Notebooks.objects.filter(nombre__contains=result)
        amplificadores=Amplificadores.objects.filter(nombre__contains=result)
        monitores=Monitores.objects.filter(nombre__contains=result)
        return render(req, "index.html", {"notebooks":notebooks, "amplificadores":amplificadores, "monitores":monitores}) 
    else:
        return render(req, "index.html")

def addProduct(req):
    response=req.headers
    if req.method == "POST":
        if response['Referer']=='http://127.0.0.1:8000/AppCoder/amplificador/agregar/':
            newProduct= AmplificadoresForm(req.POST, req.FILES)
            if newProduct.is_valid():
                newProduct.save()
                return redirect("Inicio")
        elif response['Referer']=='http://127.0.0.1:8000/AppCoder/monitor/agregar/':
            newProduct= MonitoresForm(req.POST, req.FILES)
            if newProduct.is_valid():
                newProduct.save()
                return redirect("Inicio")
        elif response['Referer']=='http://127.0.0.1:8000/AppCoder/notebook/agregar/':
            newProduct= NotebooksForm(req.POST, req.FILES)
            if newProduct.is_valid():
                product=newProduct.save()
                return redirect("Inicio")
    elif response['Referer']=='http://127.0.0.1:8000/AppCoder/amplificadores/':
        newProduct= AmplificadoresForm()
        return render(req,"addProduct.html", {'newProduct':newProduct} )
    elif response['Referer']=='http://127.0.0.1:8000/AppCoder/monitores/':
        newProduct= MonitoresForm()
        return render(req,"addProduct.html", {'newProduct':newProduct} )
    elif response['Referer']=='http://127.0.0.1:8000/AppCoder/notebooks/':
        newProduct= NotebooksForm()
        return render(req,"addProduct.html", {'newProduct':newProduct} )
    

class MonitorsListView(ListView):
    model= Monitores
    context_object_name= "productos"
    template_name= "monitores.html"

class MonitorDetailView(DetailView):
    model= Monitores
    context_object_name= "producto"
    template_name="productDetail.html"
    
class MonitorUpdateView(UpdateView):
    model = Monitores
    template_name = 'editProduct.html'
    form_class = MonitoresForm
    success_url = reverse_lazy('Monitores')
    
class MonitorDeleteView(DeleteView):
    model = Monitores
    context_object_name= "producto"
    template_name = 'deleteProduct.html'
    success_url = reverse_lazy('Monitores')
    
class NotebooksListView(ListView):
    model= Notebooks
    context_object_name= "productos"
    template_name= "notebooks.html"

class NotebooksDetailView(DetailView):
    model= Notebooks
    context_object_name= "producto"
    template_name="productDetail.html"
    
class NotebookUpdateView(UpdateView):
    model = Notebooks
    template_name = 'editProduct.html'
    form_class = NotebooksForm
    success_url = reverse_lazy('Notebooks')
    
class NotebookDeleteView(DeleteView):
    model = Notebooks
    context_object_name= "producto"
    template_name = 'deleteProduct.html'
    success_url = reverse_lazy('Notebooks')

class AmplifiersListView(ListView):
    model= Amplificadores
    context_object_name= "productos"
    template_name= "amplificadores.html"

class AmplifiersDetailView(DetailView):
    model= Amplificadores
    context_object_name= "producto"
    template_name="productDetail.html"
    
class AmplifierUpdateView(UpdateView):
    model = Amplificadores
    template_name = 'editProduct.html'
    form_class = AmplificadoresForm
    success_url = reverse_lazy('Amplificadores')
    
class AmplifierDeleteView(DeleteView):
    model = Amplificadores
    context_object_name= "producto"
    template_name = 'deleteProduct.html'
    success_url = reverse_lazy('Amplificadores')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Inicio")
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect("Inicio")

def user_register(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        print("form", form.errors)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UsuariosForm()
    return render(request, 'register.html', {'form': form})

class Profile(TemplateView):
    template_name= "profile.html"
    
@login_required
def editProfile(request):
    if request.method == 'POST':
        editProfileForm = UserEditForm(request.POST, instance=request.user)
        if editProfileForm.is_valid():
            editProfileForm.save()
            return render(request, "profile.html")
    else:
        editProfileForm = UserEditForm(instance=request.user)
    return render(request, "editProfile.html", {"editProfileForm": editProfileForm})


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    form_class= PasswordEditForm
    template_name = 'editPass.html'
    success_url = reverse_lazy('profile')
    
    
def myProducts(req):
    notebooks=Notebooks.objects.filter(user=req.user)
    amplificadores=Amplificadores.objects.filter(user=req.user)
    monitores=Monitores.objects.filter(user=req.user)
    if notebooks.exists() or amplificadores.exists() or monitores.exists():
        return render(req, "myProducts.html", {"notebooks":notebooks, "amplificadores":amplificadores, "monitores":monitores})
    else:
        noData="Aun no ingresaste productos"
        return render(req, "myProducts.html", {"noData": noData})