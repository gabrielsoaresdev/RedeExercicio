from django.shortcuts import render, redirect
from core.models import *

# Create your views here.

def index(request):
	return render(request,'index.html', {'title':'Página inicial'})

def persons(request):
	lista = Person.objects.all()
	return render(request, 'persons.html', {'lista':lista})

def add_persons(request):
	if request.method == 'POST':
		person = Person()
		person.first_name = request.POST.get('first_name')
		person.last_name = request.POST.get('last_name')
		person.age = request.POST.get('age')
		person.save()
		return redirect('/persons/')
	else:
		title = 'Cadastro de Pessoas'

	return render(request, 'person_add.html', {'title':title})

def edit_person(request, person_id):
	person = Person.objects.get(id=int(person_id))
	if request.method == 'POST':
		person.first_name = request.POST.get('first_name')
		person.last_name = request.POST.get('last_name')
		person.age = request.POST.get('age')
		person.save()
	else:
		title = 'Edicao de Pessoa'
	return render(request, 'person_edit.html', {'title':title, 'person':person})
