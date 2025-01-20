# django-hospital
Educativo y de Aprendizaje Personal

---
## Tabla de Contenidos
- [Tecnologías](#Tecnologías)
- [Configuración Inicial](#configuración-Inicial)
- [Creación del Modelo](#creación-del-modelo)
---
# Tecnologías
- Django: Framework web en Python.
- postgresql: PostgreSQL
--- 
# Configuración Inicial 
1. Entorno virtual 
    ```bash 
    python -m venv venv

2. Activar el entorno virtual
    ```bash 
    venv\Scripts\activate

3. Agregamos el requeriments.txt
    ```bash 
    asgiref==3.8.1
    attrs==24.3.0
    certifi==2024.12.14
    charset-normalizer==3.4.1
    Django==5.1.5
    django-cors-headers==4.6.0
    djangorestframework==3.15.2
    drf-spectacular==0.28.0
    idna==3.10
    inflection==0.5.1
    jsonschema==4.23.0
    jsonschema-specifications==2024.10.1
    PyYAML==6.0.2
    referencing==0.36.1
    requests==2.32.3
    rpds-py==0.22.3
    sqlparse==0.5.3
    tzdata==2024.2
    uritemplate==4.1.1
    urllib3==2.3.0
    
        
4. Actualizamos los pip
    ```bash
    python.exe -m pip install --upgrade pip

5. Instamos las dependencias del archivo requirements.txt
    ```bash
    pip install -r requirements.txt 

6. Se crea la carpeta GestionHospital
    ```bash
    mkdir GestionHospital

7. Crear el proyecto de django backend
    ```bash 
    django-admin startproject backend

8. Ingresamos al backend
    ```bash 
    cd backend

9. Creamos la aplicacion llamada api_hospital
    ```bash     
    python manage.py startapp api_hospital


10. Configuración de backend/settings.py 
    ```bash 
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',
        'rest_framework',
        'drf_spectacular',
        'api_hospital', 
    ]
    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }

    SPECTACULAR_SETTINGS = {
        'TITLE': 'Hospital Management API',
        'DESCRIPTION': 'API para la gestión de pacientes, médicos y citas en un hospital.',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,  # Si False, no incluye el esquema JSON directamente en el endpoint /schema/
        'SCHEMA_PATH_PREFIX': '/api/',  # Prefijo para limitar qué endpoints incluir en la documentación.
        'SORT_OPERATIONS': True,  # Ordena las operaciones alfabéticamente en Swagger UI.
        'SORT_TAGS': True,  # Ordena las etiquetas de los endpoints alfabéticamente.
        'COMPONENT_SPLIT_REQUEST': True,  # Separa los serializers de solicitud y respuesta si son diferentes.
    
        'DISABLE_ERRORS_AND_WARNINGS': False,  # Activa/desactiva errores y advertencias en la generación del esquema.
        'ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE': True,  # Añade opciones explícitas de null/blank a los enumerados.
        'POSTPROCESSING_HOOKS': [],  # Lista de funciones para modificar el esquema después de generarlo.
    }
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
# Creación del Modelo 

11. creamos el archivo en api_hospital/models.py
    ```bash
    from django.db import models

    class Paciente(models.Model):
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        fecha_nacimiento = models.DateField()
        sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
        telefono = models.CharField(max_length=15)
        direccion = models.TextField()

        def __str__(self):
            return f"{self.nombre} {self.apellido}"


    class Medico(models.Model):
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        especialidad = models.CharField(max_length=100)
        telefono = models.CharField(max_length=15)
        correo = models.EmailField()

        def __str__(self):
            return f"Dr. {self.nombre} {self.apellido}"


    class Cita(models.Model):
        paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
        medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas')
        fecha_hora = models.DateTimeField()
        motivo = models.TextField()
        estado = models.CharField(max_length=15, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')])

        def __str__(self):
            return f"Cita de {self.paciente} con {self.medico} el {self.fecha_hora}"

12. En api_hospital/views.py
    ```bash
    from rest_framework import viewsets
    from .models import Paciente, Medico, Cita
    from .serializers import PacienteSerializer, MedicoSerializer, CitaSerializer

    class PacienteViewSet(viewsets.ModelViewSet):
        queryset = Paciente.objects.all()
        serializer_class = PacienteSerializer

    class MedicoViewSet(viewsets.ModelViewSet):
        queryset = Medico.objects.all()
        serializer_class = MedicoSerializer

    class CitaViewSet(viewsets.ModelViewSet):
        queryset = Cita.objects.all()
        serializer_class = CitaSerializer

13. Agregamos al proyecto api_hospital/urls.py
    ```bash	
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import PacienteViewSet, MedicoViewSet, CitaViewSet

    router = DefaultRouter()
    router.register(r'pacientes', PacienteViewSet)
    router.register(r'medicos', MedicoViewSet)
    router.register(r'citas', CitaViewSet)

    urlpatterns = [
        path('api/', include(router.urls)),
    ]
14. api_hospital/admin.py
    ```bash
    from django.contrib import admin
    from .models import Paciente, Medico, Cita

    admin.site.register(Paciente)
    admin.site.register(Medico)
    admin.site.register(Cita)

15. migrar en la base de datos
    ```bash 
    python manage.py migrate
    python manage.py makemigrations
    python manage.py migrate

16. Creamos un aplicacion en docs
    ```bash	
    python manage.py startapp docs

17. Agregamos todas las aplicaciones y configuraciones al backend/settings.py 
    ```bash
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'corsheaders',
            'rest_framework',
            'drf_spectacular',
            'api_hospital',
            'docs',
        ]

        REST_FRAMEWORK = {
            'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
        }

        SPECTACULAR_SETTINGS = {
            'TITLE': 'Hospital Management API',
            'DESCRIPTION': 'API para la gestión de pacientes, médicos y citas en un hospital.',
            'VERSION': '1.0.0',
            'SERVE_INCLUDE_SCHEMA': False,  # Si False, no incluye el esquema JSON directamente en el endpoint /schema/
            'SCHEMA_PATH_PREFIX': '/api/',  # Prefijo para limitar qué endpoints incluir en la documentación.
            'SORT_OPERATIONS': True,  # Ordena las operaciones alfabéticamente en Swagger UI.
            'SORT_TAGS': True,  # Ordena las etiquetas de los endpoints alfabéticamente.
            'COMPONENT_SPLIT_REQUEST': True,  # Separa los serializers de solicitud y respuesta si son diferentes.
        
            'DISABLE_ERRORS_AND_WARNINGS': False,  # Activa/desactiva errores y advertencias en la generación del esquema.
            'ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE': True,  # Añade opciones explícitas de null/blank a los enumerados.
            'POSTPROCESSING_HOOKS': [],  # Lista de funciones para modificar el esquema después de generarlo.
        }

18. creamos la urls.py en docs/urls.py 
    ```bash
    from django.urls import path
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

    # Definición de las rutas para la generación y visualización de la documentación de la API
    urlpatterns = [
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]

19. Ingresamos la nueva url en backend/urls.py 
    ```bash 
    from django.contrib import admin
    from django.urls import path,include

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('api_hospital.urls')),
        path('', include('docs.urls')),
    ]


20. Creamos un .env en el archivo principal
    ```bash
    DATABASE_NAME=test3
    DATABASE_USER=postgres
    DATABASE_PASSWORD=tucontrasenia
    DATABASE_HOST=localhost
    DATABASE_PORT=5432

21. Instalamos django-decouple
    ```bash
    pip install django-decouple

22. Nos vamos al principio antes del crud y guardamos la dependecia
    ```bash
    pip freeze > requirements.txt

23. en el crud/settings.py configuramos la base de datos en postgrest
    ```bash
    from decouple import config
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST'),
            'PORT': config('DATABASE_PORT'),
        }
    }

24. Generamos el proyecto frontend
    ```bash
    django-admin startproject frontend

25. Entramos a frontend
    ```bash
    cd frontend

26. Creamos la aplicación 
     ```bash
    python manage.py startapp hospital 

27. frontend/settings.py 
    ```bash	
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hospital',
    ]

28. frontend/urls.py
    ```bash	
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('hospital.urls')),
    ]
29. frontend/hospital/
    ```bash
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

30. frontend/hospital/urls.py
    ```bash
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('citas/', views.citas_list, name='citas_list'),
        path('citas/<int:id>/', views.citas_detail, name='citas_detail'),
        path('citas/create/', views.citas_create, name='citas_create'),
        path('medicos/', views.medicos_list, name='medicos_list'),
    ]
