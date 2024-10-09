from django.contrib import admin
from django.urls import path
from agendamentos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendar/', views.agendar, name='agendar'),
    path('listar_agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('adicionar_dia/', views.adicionar_dia_disponivel, name='adicionar_dia_disponivel'),
]
