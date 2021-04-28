from django.shortcuts import render, redirect
#import . from biz_layer.Conversor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home_usuario(request, username, repeticiones):
    context = {'username': username,
     'lastname': 'frias',
     'repeticiones': range(repeticiones),
     'colores': ['rojo', 'azul', 'verde']
     }
    return render(request,'usuario.html', context)

def create_user(request):        
    nombreUsuario =  request.POST['name']
    request.session['username'] = nombreUsuario
    print (request.session['username'])
    return redirect('/show_user')

def show_user(request):
    print ('username: ', request.session['username'])
    return render(request,'home_usuario.html')
