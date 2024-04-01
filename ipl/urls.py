"""
URL configuration for ipl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from csk.views import *
from rcb.views import *
from mi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msd/',msd,name='msd'),
    path('virat/',virat,name='virat'),
    path('rohit/',rohit,name='rohit',),
    path('rutu/',rutu,name='rutu'),
    path('karthik/',karthik,name='karthik'),
    path('hardik/',hardik,name='hardik'),
]
