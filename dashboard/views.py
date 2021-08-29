from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . models import Notes
from . forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import requests
from isodate import parse_duration
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,'dashboard/home.html')

@login_required
def notes(request):
    if request.method=='POST':
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username} successfully")    

    else:
        form=NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={"notes":notes,"form":form}
    return render(request,'dashboard/notes.html',context)

@login_required   
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model=Notes

@login_required   
def homework(request):
    if request.method=="POST":
        form=HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=="on":
                    finished=True
                else:
                    finished=False    
            except:
                finished=False
            homework=Homework(user=request.user,subject=request.POST['subject'],title=request.POST['title'],description=request.POST['description'],due=request.POST['due'],is_finished=finished)     
            homework.save()
            messages.success(request,f"Homework Added!!")       
    else:
        form=HomeworkForm()
    homework=Homework.objects.filter(user=request.user)
    if len(homework)==0:
        homework_done=True
    else:
        homework_done=False 
           
    context={"homeworks":homework,"homeworks_done":homework_done,"form":form,}
    return render(request,'dashboard/homework.html',context)

@login_required   
def update_hw(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished==True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()
    return redirect('homework')       

@login_required   
def delete_hw(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')    

@login_required   
def todo(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            todos=Todo(user=request.user,title=request.POST['title'],is_finished=finished)    
            todos.save()
            messages.success(request,f"Tasks added!!")
    else:
        form=TodoForm()
    todo=Todo.objects.filter(user=request.user)    
    if len(todo)==0:
        todos_done=True
    else:
        todos_done=False 
   
    context={"todos":todo,'todos_done':todos_done,"form":form,}
    return render(request,'dashboard/todo.html',context) 

@login_required   
def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()
    return redirect('todo')  

@login_required   
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def books(request):
    return render(request,'dashboard/books.html') 

def register(request):
    form=UserCreationForm()
    context={"form":form}
    return render(request,'dashboard/register.html',context) 


def profile(request):
    homework=Homework.objects.filter(is_finished=False,user=request.user)
    todo=Todo.objects.filter(is_finished=False,user=request.user)
    if len(homework)==0:
        homework_done=True
    else:
        homework_done=False 

    if len(todo)==0:
        todos_done=True
    else:
        todos_done=False     
    context={"homework":homework,"todo":todo,"homework_done":homework_done,"todos_done":todos_done}    
    return render(request,'dashboard/profile.html',context)