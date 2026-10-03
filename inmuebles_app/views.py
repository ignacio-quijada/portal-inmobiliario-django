from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import InmuebleForm, RegistroUsuarioForm, UserUpdateForm, PerfilUpdateForm
from .models import Inmueble, Perfil, Region, Comuna

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(
                usuario=user,
                tipo_usuario=form.cleaned_data['tipo_usuario'],
                rut=form.cleaned_data['rut'],
                telefono=form.cleaned_data['telefono']
            )
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_view(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, instance=perfil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'perfil': perfil
    }
    return render(request, 'perfil.html', context)

@login_required
def nuevo_inmueble_view(request):
    if request.user.perfil.tipo_usuario != 'arrendador':
        return redirect('catalogo')
    
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user
            inmueble.save()
            return redirect('perfil')
    else:
        form = InmuebleForm()
    return render(request, 'nuevo_inmueble.html', {'form': form})

@login_required
def lista_inmuebles_view(request):
    if request.user.perfil.tipo_usuario != 'arrendador':
        return redirect('catalogo')   
    inmuebles = Inmueble.objects.filter(propietario=request.user)
    return render(request, 'lista_inmuebles.html', {'inmuebles': inmuebles})

@login_required
def actualizar_inmueble_view(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id, propietario=request.user)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('lista_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'actualizar_inmueble.html', {'form': form, 'inmueble': inmueble})

@login_required
def eliminar_inmueble_view(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id, propietario=request.user)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('lista_inmuebles')
    return redirect('lista_inmuebles')

def catalogo_inmuebles_view(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    inmuebles = Inmueble.objects.filter(disponible=True)

    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')

    if region_id:
        inmuebles = inmuebles.filter(comuna__region_id=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(comuna_id=comuna_id)

    context = {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas,
    }
    return render(request, 'catalogo_inmuebles.html', context)