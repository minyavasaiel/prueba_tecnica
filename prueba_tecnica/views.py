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
        #pendiente comprobar si la organización ya existe en la base de datos
        for organization in organizations:
            newOrganization = Organization(name=organization['name'], contact=organization['contact'], phone=organization['Phone'])
            newOrganization.save()
           
            # parte de los centros de la organización
            centres = organization["Centres"]
            for center in centres:
                newCenter = Center(name=center['name'], stories=center['stories'], organization=newOrganization)
                newCenter.save()