from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home (request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products})

def about(request):
	return render(request, 'about.html', {})	

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión con éxito. Gracias.")
            return redirect('home')
        else:
            messages.error(request, "Hubo un problema, por favor intenta nuevamente.")
            return redirect('login')  # Me lleva al 'login' 

    # Si la solicitud es GET, renderiza el formulario de inicio de sesión
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado sesión con éxito. Gracias por visitarnos.")
    return redirect('home')