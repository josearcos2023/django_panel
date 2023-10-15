from django.urls import path

from . import views
from django.urls import include

app_name = 'web'

urlpatterns = [
     path('', views.AlumnoView.as_view(),name='index'),
     path("registrarAlumno/", views.registrarAlumno),
     path("edicionAlumno/<codigo>", views.edicionAlumno),
     path("editarAlumno/", views.editarAlumno),
     path("eliminacionAlumno/<codigo>", views.eliminarAlumno),
     path('listaProfesores/', views.ProfesorView.as_view(),name='listaProfesores'),
     path("listaProfesores/registrarProfesor/", views.registrarProfesor),
     path("listaProfesores/edicionProfesor/<codigo>", views.edicionProfesor),
     path("listaProfesores/editarProfesor/", views.editarProfesor),
     path("listaProfesores/eliminacionProfesor/<codigo>", views.eliminarProfesor),
]