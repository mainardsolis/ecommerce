from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm

'''





def register_user(request):
	
	 form = SignUpForm(request.POST)
          if form.is_valid():
                  form.save()
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password1']
                  # iniciar sesion
                  user = authenticate(username=username, password=password)
                  login(request, user)
                  messages.success(request, ("Usuario Registrado satisfactoriamente.Bienvenido!"))
                  return redirect('update_info')
          else:
                  messages.success(request, ("Whoops! Hubo un problema al registrarte, por favor intenta nuevamente..."))
                  return redirect('register')
		
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
			return redirect('update_info')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})	


'''


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

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # logueo de usuario
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Usuario Registrado satisfactoriamente.Bienvenido!"))
            return redirect('home')
        else:
            messages.success(request, ("Whoops!Hubo un problema al registrarte, por favor intenta nuevamente..."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})

def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})