from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    if request.method == 'POST':
        taskTitle = request.POST['title']
        taskDesc = request.POST['desc']
        ins = Task(taskTitle=taskTitle, taskDesc=taskDesc)
        ins.save()

    return render(request, 'index.html')

def tasks(request):
    return render(request, 'tasks.html')
