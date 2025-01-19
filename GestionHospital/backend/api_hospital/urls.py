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