import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

API_BASE_URL = "http://localhost:8000/api/"  # Cambiar según el entorno

def index(request):
    return render(request, 'hospital/index.html')

def citas_list(request):
    response = requests.get(f"{API_BASE_URL}citas/")
    citas = response.json()
    return render(request, 'hospital/citas_list.html', {'citas': citas})

def citas_detail(request, id):
    response = requests.get(f"{API_BASE_URL}citas/{id}/")
    cita = response.json()
    return render(request, 'hospital/citas_detail.html', {'cita': cita})

def citas_create(request):
    if request.method == "POST":
        data = {
            'paciente': request.POST['paciente'],
            'medico': request.POST['medico'],
            'fecha_hora': request.POST['fecha_hora'],
            'motivo': request.POST['motivo'],
            'estado': request.POST['estado'],
        }
        response = requests.post(f"{API_BASE_URL}citas/", json=data)
        if response.status_code == 201:
            return redirect('citas_list')
    medicos = requests.get(f"{API_BASE_URL}medicos/").json()
    pacientes = requests.get(f"{API_BASE_URL}pacientes/").json()
    return render(request, 'hospital/citas_create.html', {'medicos': medicos, 'pacientes': pacientes})

def medicos_list(request):
    response = requests.get(f"{API_BASE_URL}medicos/")
    medicos = response.json()
    return render(request, 'hospital/medicos_list.html', {'medicos': medicos})