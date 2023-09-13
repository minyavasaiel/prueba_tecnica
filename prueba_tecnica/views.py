from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Organization, Center
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
    return render(request, 'listar.html', {'organizations': organizations})

def listarCentros(request):
    #obtener todos los elementos
    centers = Center.objects.all()
    return render(request, 'listar-centros.html', {'centers': centers})