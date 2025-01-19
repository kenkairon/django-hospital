from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('citas/', views.citas_list, name='citas_list'),
    path('citas/<int:id>/', views.citas_detail, name='citas_detail'),
    path('citas/create/', views.citas_create, name='citas_create'),
    path('medicos/', views.medicos_list, name='medicos_list'),
]