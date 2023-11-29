# En tu views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from inmo.models import Propiedad, Compra, ComunaPropiedad, ContratoPropiedad, TipoPropiedad
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from datetime import datetime
from django.http import HttpResponseBadRequest  # Importamos HttpResponseBadRequest

# Función de validación de enteros
def validar_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return None

def home(request):
    return render(request, "index.html", {'nbar': 'home'})

def propiedades(request):
    propiedadListados = Propiedad.objects.all()

    datos = {
        'propiedad': propiedadListados, 
    }

    return render(request, 'propiedades.html', {"datos": datos,'nbar': 'propiedades'})

def propiedadesUsuario(request):
    countpropiedades = Propiedad.objects.filter(owner=request.user).count()
    propiedadListados = Propiedad.objects.filter(owner=request.user)

    datos = {
        'propiedad': propiedadListados,
        'countpropiedades': countpropiedades, 
    }

    return render(request, 'propiedadesusuario.html', {"datos": datos,'nbar': 'propiedadesUsuario'})

def propiedad(request, propiedad_id):
    propiedad = Propiedad.objects.get(propiedad_id=propiedad_id)
    datos = {'propiedad' : propiedad}
    return render(request, "propiedad.html", {"datos":datos})

# ...

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('../login/')
    else:
        form = UserRegisterForm()
        
    data = {'form': form}
    return render(request,"registro.html", data)

@login_required(login_url='../login/')
def fC(request, propiedad_id):
    propiedad = Propiedad.objects.get(propiedad_id=propiedad_id)
    datos = {'propiedad': propiedad}
    return render(request, "Formulario_compra.html",{"datos":datos})

def compra(request):
    propiedad_id=request.POST['propiedad_id']
    tipo_pago=request.POST['tipo_pago']
    numero=request.POST['numero']
    comentario=request.POST['message']

    compra = Compra.objects.create(
        propiedad_id=propiedad_id,
        cliente=request.user,
        tipo_pago=tipo_pago,
        numero=numero,
        comentario=comentario,
    )
    return redirect('/')

# ...

def mi_cuenta(request):
    propiedadListados = Propiedad.objects.filter(owner=request.user)
    countpropiedades = Propiedad.objects.filter(owner=request.user).count()

    datos = {
        'propiedad': propiedadListados, 
        'countpropiedades':countpropiedades,
        'user': request.user,
        'hora': datetime.now().strftime('%H:%M'),   
    }

    return render(request, "mi-cuenta.html", {"datos":datos})

def mi_configuracion(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('../mi_cuenta/inicio')
    else:
        form = EditProfileForm(instance=request.user)
        datos = {'form':form}
        return render(request, "configurar.html", datos)

#################################################################################

def paneladmin (request):
    listar_c = ComunaPropiedad.objects.all()
    listar_p = Propiedad.objects.all()
    listar_ct = ContratoPropiedad.objects.all()
    listar_usr = User.objects.all()
    listar_con = Compra.objects.all()

    datos = {
        'listar_c' : listar_c,
        'listar_p' : listar_p,
        'listar_ct' : listar_ct,
        'listar_usr' : listar_usr,
        'listar_con' : listar_con,
        'hora': datetime.now().strftime('%H:%M'),
    }
    return render(request, 'panel-admin.html', {"datos": datos,'nbar': 'adminpanel'})

def lst_p (request):
    listar_c = ComunaPropiedad.objects.all()
    listar_p = Propiedad.objects.all()
    listar_ct = ContratoPropiedad.objects.all()

    datos = {
        'listar_c' : listar_c,
        'listar_p' : listar_p,
        'listar_ct' : listar_ct,
    }
    return render(request, 'crud_propiedad.html', {"datos": datos,'nbar': 'adminpanel'})

def lst_c (request):
    listar_c = ComunaPropiedad.objects.all()
    listar_p = Propiedad.objects.all()
    listar_ct = ContratoPropiedad.objects.all()

    datos = {
        'listar_c' : listar_c,
        'listar_p' : listar_p,
        'listar_ct' : listar_ct,
    }
    return render(request, 'crud_comunas.html', {"datos": datos,'nbar': 'adminpanel'})

def lst_usr(request):
    listar_usr = User.objects.all()

    datos = {
        'listar_usr' : listar_usr,
    }
    return render(request, 'crud_users.html', {"datos": datos,'nbar': 'adminpanel'})

def crearP(request):
    listar_c = ComunaPropiedad.objects.all()
    listar_p = Propiedad.objects.all()
    listar_ct = ContratoPropiedad.objects.all()
    listar_tp = TipoPropiedad.objects.all()

    datos = {
        'listar_c' : listar_c,
        'listar_p' : listar_p,
        'listar_ct' : listar_ct,
        'listar_tp' : listar_tp,
    }
    return render(request, 'crear_p.html', {"datos": datos})

def registrar_propiedad(request):
    idComuna = request.POST['idComuna']
    idTipo = request.POST['idTipo']
    idContrato = request.POST['idContrato']
    direccion = request.POST.get('txt_direccion')
    imagen1 = request.POST.get('url_img1')
    imagen2 = request.POST.get("url_img2")
    num_dor = request.POST.get('num_dor')
    num_banos = request.POST.get('num_banos')
    num_estac = request.POST.get('num_estac')
    precio = request.POST.get('precio')
    descripcion = request.POST.get('descripcion')
    disponible = request.POST.get('disponible')

    objComuna = ComunaPropiedad()
    objComuna.idComuna = idComuna

    objTipopropiedad = TipoPropiedad()
    objTipopropiedad.idTipo = idTipo

    objContrato = ContratoPropiedad()
    objContrato.idContrato = idContrato

    if disponible == '1':
        disponiblee = True
    else:
        disponiblee = False

    propiedad = Propiedad.objects.create(
        comuna = objComuna,
        tipo_negocio = objTipopropiedad,
        tipoContrato = objContrato,
        direccion = direccion,
        imagen = imagen1,
        imagen2 =imagen2,
        num_dor = num_dor,
        num_banios = num_banos,
        num_estac = num_estac,
        precio = precio,
        descripcion = descripcion,
        disponible = disponiblee
    )
    return redirect('../propiedades')

def contactado(request,compra_id):
    compra = Compra.objects.get(compra_id = compra_id)

    compra.contactado = True
    compra.save()

    return redirect('../inicio')

def edicionPropiedad(request,propiedad_id):
    propiedad = Propiedad.objects.get(propiedad_id = propiedad_id)
    listar_c = ComunaPropiedad.objects.all()
    listar_p = Propiedad.objects.all()
    listar_ct = ContratoPropiedad.objects.all()
    listar_tp = TipoPropiedad.objects.all()
    

    datos = {
        'listar_c' : listar_c,
        'listar_p' : listar_p,
        'listar_ct' : listar_ct,
        'listar_tp' : listar_tp,
    }
    return render(request, 'edicionP.html', {"propiedad" : propiedad,"datos": datos})

def editarP(request):
    propiedad_id = request.POST.get('propiedad_id')
    idComuna = request.POST['idComuna']
    idTipo = request.POST['idTipo']
    idContrato = request.POST['idContrato']
    direccion = request.POST.get('txt_direccion')
    imagen1 = request.POST.get('url_img1')
    imagen2 = request.POST.get("url_img2")
    num_dor = request.POST.get('num_dor')
    num_banos = request.POST.get('num_banos')
    num_estac = request.POST.get('num_estac')
    precio = request.POST.get('precio')
    descripcion = request.POST.get('descripcion')
    disponible = request.POST.get('disponible')


    objComuna = ComunaPropiedad()
    objComuna.idComuna = idComuna

    objTipopropiedad = TipoPropiedad()
    objTipopropiedad.idTipo = idTipo

    objContrato = ContratoPropiedad()
    objContrato.idContrato = idContrato

    propiedad = Propiedad.objects.get(propiedad_id = propiedad_id)

    propiedad.comuna = objComuna
    propiedad.tipo_negocio = objTipopropiedad
    propiedad.tipoContrato = objContrato
    propiedad.direccion = direccion
    propiedad.imagen = imagen1
    propiedad.imagen2 =imagen2
    propiedad.num_dor = num_dor
    propiedad.num_banios = num_banos
    propiedad.num_estac = num_estac
    propiedad.precio = precio
    propiedad.descripcion = descripcion
    if disponible == '1':
        propiedad.disponible = True
    else:
        propiedad.disponible = False
    propiedad.save()

    return redirect('../propiedades')


def eliminarPropiedad(request,propiedad_id):
    propiedad = Propiedad.objects.get(propiedad_id=propiedad_id)
    propiedad.delete()
    return redirect('../propiedades')

########## COMUNA ###############

def edicionComuna(request,comuna_id):

    comuna = ComunaPropiedad.objects.get(idComuna = comuna_id)

    return render(request, 'edicionC.html', {"comuna" : comuna})

def editarC(request):
    comuna_id = request.POST.get('comuna_id')
    nombre = request.POST.get('txt_nombre')
    comuna = ComunaPropiedad.objects.get(idComuna = comuna_id)
    comuna.nombreComuna = nombre
    comuna.save()

    return redirect('../comunas')

def eliminarComuna(request,comuna_id):
    comuna = ComunaPropiedad.objects.get(idComuna=comuna_id)
    comuna.delete()
    return redirect('../comunas')

def crearC(request):
    listar_c = ComunaPropiedad.objects.all()

    datos = {
        'listar_c' : listar_c,
        'nbar': 'adminpanel',  # Agregamos 'nbar' para seguridad
    }
    return render(request, 'crear_c.html', {"datos": datos})

def registrar_comuna(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comuna = ComunaPropiedad.objects.create(nombreComuna=nombre)
            return redirect('../comunas')
    else:
        form = ComunaForm()

    return render(request, 'crear_c.html', {'form': form, 'nbar': 'adminpanel'})  # Agregamos 'nbar' para seguridad

# ...
