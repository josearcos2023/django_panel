from django.shortcuts import render, redirect

from django.views import View
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')

def registrarAlumno(request):
    codigo=request.POST['txtId']
    nombre=request.POST['txtNombre']
    email=request.POST['txtEmail']
    alumno=TblAlumno.objects.create(
        alumno_id=codigo, alumno_nombre=nombre, alumno_email=email
    )
    messages.success(request, 'Alumno Registrado!!')

    return redirect('/')

def eliminarAlumno(request, codigo):
    alumno=TblAlumno.objects.get(alumno_id=codigo)
    alumno.delete()
    messages.success(request, 'Alumno Eliminado!!')

    return redirect('/')

def edicionAlumno(request, codigo):
    alumno=TblAlumno.objects.get(alumno_id=codigo)
    return render(request, "edicionAlumno.html", {"alumno":alumno})

def editarAlumno(request):
    codigo=request.POST['txtId']
    nombre=request.POST['txtNombre']
    email=request.POST['txtEmail']
    
    alumno=TblAlumno.objects.get(alumno_id=codigo)
    alumno.alumno_nombre=nombre
    alumno.alumno_email=email
    alumno.save()
    messages.success(request, 'Alumno Actualizado!!')

    return redirect('/')

class ProfesorView(View):
    
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'listaProfesores.html',context)

    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('/')

def registrarProfesor(request):
    codigo=request.POST['txtId']
    nombre=request.POST['txtNombre']
    email=request.POST['txtEmail']
    profesor=TblProfesor.objects.create(
        profesor_id=codigo, profesor_nombre=nombre, profesor_email=email
    )
    messages.success(request, 'Alumno Registrado!!')

    return redirect('/')
        
def eliminarProfesor(request, codigo):
    profesor=TblProfesor.objects.get(profesor_id=codigo)
    profesor.delete()
    messages.success(request, 'Registro de Profesor Eliminado!!')

    return redirect('/listaProfesores')

def edicionProfesor(request, codigo):
    profesor=TblProfesor.objects.get(profesor_id=codigo)
    return render(request, "edicionProfesor.html", {"profesor":profesor})

def editarProfesor(request):
    codigo=request.POST['txtId']
    nombre=request.POST['txtNombre']
    email=request.POST['txtEmail']
    
    profesor=TblProfesor.objects.get(profesor_id=codigo)
    profesor.profesor_nombre=nombre
    profesor.profesor_email=email
    profesor.save()
    messages.success(request, 'Profesor Actualizado!!')

    return redirect('/listaProfesores')