from django.shortcuts import render, redirect
from .models import Comunidad, Usuarios
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def signUp(request):
    if request.method == 'GET':
        print('holsss')
        return render(request, 'signUp.html', {"form": UserCreationForm})
    else:
        print(request.POST)
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('adminPanel')
            except IntegrityError:
                return render(request, 'signUp.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signUp.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    
def signIn(request):
    if request.method == 'GET':
        return render(request, 'signIn.html', {
            'form': AuthenticationForm
    })
    else:
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signIn.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
        })
        login(request, user)
        return redirect('adminPanel')

def home(request):
    return render(request, 'home.html')

@login_required
def signOut(request):
    logout(request)
    return redirect('/')

@login_required
def adminPanel(request):
    return render(request, 'adminPanel.html')

@login_required
def gestionUsuarios(request):
    usuariosList = Usuarios.objects.all()
    return render(request, 'gestionUsuarios.html', {"usuarios":usuariosList})

@login_required
def registrarUsuarios(request):
    codigo=request.POST['txtCodigo']
    cedula=request.POST['txtCedula']
    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    domicilio=request.POST['txtDomicilio']
    email=request.POST['txtEmail']
    telefono=request.POST['txtTelefono']
    rol=request.POST['rols']
    comunidad=request.POST['comunidades']

    Usuarios.objects.create(
        codigo=codigo, cedula=cedula, nombres=nombres, apellidos=apellidos, domicilio=domicilio, email=email,telefono=telefono,rol=rol, comunidad=comunidad )
    return redirect('gestionUsuarios')

@login_required
def editarUsuarios(request, codigo):
    usuarios= Usuarios.objects.get(codigo=codigo)
    return render(request, 'edicionUsuarios.html', {"usuarios":usuarios})

@login_required
def edicionUsuarios(request):
    codigo=request.POST['txtCodigo']
    cedula=request.POST['txtCedula']
    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    domicilio=request.POST['txtDomicilio']
    email=request.POST['txtEmail']
    telefono=request.POST['txtTelefono']
    rol=request.POST['rols']
    comunidad=request.POST['comunidades']

    usuarios= Usuarios.objects.get(codigo=codigo)
    usuarios.cedula = cedula
    usuarios.nombres = nombres
    usuarios.apellidos = apellidos
    usuarios.domicilio = domicilio
    usuarios.email = email
    usuarios.telefono = telefono
    usuarios.rol = rol
    usuarios.comunidad = comunidad

    usuarios.save()
    return redirect('gestionUsuarios')

@login_required
def eliminarUsuarios(request, codigo):
    usuarios= Usuarios.objects.get(codigo=codigo)
    usuarios.delete()
    return redirect('gestionUsuarios')

@login_required
def gestionComunidad(request):
    comunidadesList = Comunidad.objects.all()
    return render(request, 'gestionComunidad.html', {"comunidades":comunidadesList})

@login_required
def registrarComunidad(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    sector=request.POST['txtSector']

    Comunidad.objects.create(
        codigo=codigo, nombre=nombre, sector=sector)
    return redirect('gestionComunidad')

@login_required
def editarComunidad(request, codigo):
    comunidad= Comunidad.objects.get(codigo=codigo)
    return render(request, "edicionComunidad.html", {"comunidad":comunidad})

@login_required
def edicionComunidad(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    sector=request.POST['txtSector']

    comunidad= Comunidad.objects.get(codigo=codigo)
    comunidad.nombre = nombre
    comunidad.sector = sector

    comunidad.save()
    return redirect('gestionComunidad')

@login_required
def eliminarComunidad(request, codigo):
    comunidad= Comunidad.objects.get(codigo=codigo)
    comunidad.delete()
    return redirect('gestionComunidad')

