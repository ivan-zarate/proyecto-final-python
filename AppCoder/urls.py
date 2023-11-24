from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('monitor/agregar/', views.addProduct, name='addMonitor'),
    path('amplificador/agregar/', views.addProduct, name='addAmplifier'),
    path('notebook/agregar/', views.addProduct, name='addNotebook'),
    
    
    path('monitores/', views.MonitorsListView.as_view(), name="Monitores"),
    path('monitores/<pk>', views.MonitorDetailView.as_view(), name="DetalleMonitor"),
    path('monitores/editar/<int:pk>/', views.MonitorUpdateView.as_view(), name='editar_monitor'),
    path('monitores/eliminar/<int:pk>/', views.MonitorDeleteView.as_view(), name='eliminar_monitor'),
    path('notebooks/', views.NotebooksListView.as_view(), name="Notebooks"),
    path('notebooks/<pk>', views.NotebooksDetailView.as_view(), name="DetalleNotebook"),
    path('notebooks/editar/<int:pk>/', views.NotebookUpdateView.as_view(), name='editar_notebook'),
    path('notebooks/eliminar/<int:pk>/', views.NotebookDeleteView.as_view(), name='eliminar_notebook'),
    path('amplificadores/', views.AmplifiersListView.as_view(), name="Amplificadores"),
    path('amplificadores/<pk>', views.AmplifiersDetailView.as_view(), name="DetalleAmplificador"),
    path('amplificadores/editar/<int:pk>/', views.AmplifierUpdateView.as_view(), name='editar_amplificador'),
    path('amplificadores/eliminar/<int:pk>/', views.AmplifierDeleteView.as_view(), name='eliminar_amplificador'),
    
    path('mi-perfil/', views.Profile.as_view(), name='profile'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('editar-perfil/', views.editProfile, name='editProfile'),
    path('editar-contrasenia/', views.ChangePassword.as_view(), name='editPass'),
    path('mis-productos/', views.myProducts, name='myProducts')
]
