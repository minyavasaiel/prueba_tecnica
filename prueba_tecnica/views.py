from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Organization, Center
from django.contrib.auth.decorators import login_required
import json

@login_required
def index(request):
    read_json()
    return render(request, 'crud.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def read_json():
    route_json = 'data/data.json'
    with open(route_json, 'r') as json_file:
        data = json.load(json_file)
        organizations = data['organizations']
        
        for organization in organizations:
            name = organization['name']
            existing_organization = Organization.objects.filter(name=name).first()

            if existing_organization:
            # Abandonado por posible problema de duplicado de datos
                '''existing_organization.contact = organization['contact']
                existing_organization.phone = organization['Phone']
                existing_organization.save()'''
            else:
                newOrganization = Organization(name=name, contact=organization['contact'], phone=organization['Phone'])
                newOrganization.save()
                
                # parte de los centros de la organización
                centres = organization["Centres"]
                for center in centres:
                    centerName = center['name']
                    existing_center = Center.objects.filter(name=centerName).first()

                    if existing_center:
                       # Abandonado por posible problema de duplicado de datos
                        '''existing_center.stories = center['stories']
                        existing_center.organization = newOrganization
                        existing_center.save()'''
                    else:
                        newCenter = Center(name=center['name'], stories=center['stories'], organization=newOrganization)
                        newCenter.save()

def listar(request):
    #obtener todos los elementos
    organizations = Organization.objects.all()
    return render(request, 'organizations-list.html', {'organizations': organizations})

def listarCentros(request):
    centers = Center.objects.all()
    return render(request, 'centers-list.html', {'centers': centers})

def add_center(request):
    organizations = Organization.objects.all()
    return render(request, 'add-center.html', {'organizations': organizations})

def add_organization(request):
    return render(request, 'add-organization.html', {})

def added_center(request):
    if request.method != 'POST':
        return HttpResponse('Error')
    name = request.POST['name']
    stories = request.POST['stories']
    idOrganization= request.POST['centerOrganization']
    organization = Organization.objects.get(pk=idOrganization)
    newCenter = Center(name=name, stories=stories, organization=organization)
    newCenter.save()
    return HttpResponse("Centro agregado correctamente.")

def added_organization(request):
    if request.method != 'POST':
        return HttpResponse('Error')
    name = request.POST['name']
    contact = request.POST['contact']
    phone= request.POST['phone']
    newOrganization = Organization(name=name, contact=contact, phone=phone)
    newOrganization.save()
    return HttpResponse("Organización agregada correctamente.")

def detail_center(request, id):
    center = Center.objects.get(pk=id)
    organizations = Organization.objects.all()
    return render(request, 'detail-center.html', {'center': center, 'organizations': organizations})

def detail_organization(request, id):
    organization = Organization.objects.get(pk=id)
    return render(request, 'detail-organization.html', {'organization': organization})

def updated(request, id):
    if request.method != 'POST':
        return HttpResponse('Error')
    center = Center.objects.get(pk=id)
    center.name = request.POST['name']
    center.stories = request.POST['stories']

    #organización
    idOrganization= request.POST['centerOrganization']
    newOrganization = Organization.objects.get(pk=idOrganization)
    center.organization = newOrganization
    center.save()
    return render(request, 'updated-center.html', {'center': center, 'newOrganization': newOrganization})

def updated_organization(request, id):
    if request.method != 'POST':
        return HttpResponse('Error')
    organization = Organization.objects.get(pk=id)
    organization.name = request.POST['name']
    organization.contact = request.POST['contact']
    organization.phone = request.POST['phone']
    organization.save()
    return render(request, 'updated-organization.html', {'organization': organization})

@login_required     #para evitar que borren sin estar logueados, poniendo la url
def delete_center(request, id):
    center = Center.objects.get(pk=id)
    center.delete()
    return render(request, 'deleted-center.html', {'center': center})

@login_required     #para evitar que borren sin estar logueados, poniendo la url
def delete_organization(request, id):
    organization = Organization.objects.get(pk=id)
    organization.delete()
    return render(request, 'deleted-organization.html', {'organization': organization})
        
    
  
