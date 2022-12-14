"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, segunda_vista, dia_de_hoy, saludo_con_nombre, probandohtml
from App1.views import familiar1, familiar2, familiar3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludar'),
    path('segundavista/', segunda_vista, name='segunda_vista'),
    path('diadehoy/', dia_de_hoy, name='dia_de_hoy'),
    path('saludoconnombre/<nombre>', saludo_con_nombre, name='saludo_con_nombre'),
    path('probandoTemplate/', probandohtml, name='probandohtml'),
    path('familiar1/', familiar1, name='familiar1'),
    path('familiar2/', familiar2, name='familiar2'),
    path('familiar3/', familiar3, name='familiar3'),



]