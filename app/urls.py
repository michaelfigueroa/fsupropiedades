from django.urls import path
from .views import home, contacto, galeria
#from .import views

#En la raiz del sitio ('') se cargará el view "home", quien a su vez busca el html para mostrarlo
urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    #path('', views.home, name='home'),
]