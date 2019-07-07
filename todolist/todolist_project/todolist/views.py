from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todolist
from .forms import TodolistForm
# Create your views here.
# first view #
def home(request):
    # get all item (tasks) #
    form = TodolistForm()
    all_items = Todolist.objects.all()
    return render(request,'todolist.html',{'form':form,'all_items':all_items})

def create_todo(request):
    form = TodolistForm(request.POST)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    return HttpResponse('Something goes Wrong, Please try again')

def delete_todo(request,id):
    item = Todolist.objects.get(id=id)
    item.delete()
    return redirect('/')

def update_todo(request,id):
    item = Todolist.objects.get(id=id)
    form = TodolistForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        return render(request,'edit.html',{'form':form,'item':item})

def finished_task(request,id):
    item = Todolist.objects.get(id=id)
    item.completed = True
    item.save()
    return redirect('/')

def unfinished_task(request,id):
    item = Todolist.objects.get(id=id)
    item.completed = False
    item.save()
    return redirect('/')
