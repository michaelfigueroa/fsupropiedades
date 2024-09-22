from django.shortcuts import render

# Create your views here.

# Conecta con el modelo de la bd
# ulr-->view-->template: Carga los html y los muestra al usuario

# Función que encuentra el template home
# Debe ser llamado por una URL del modulo "app"
def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')