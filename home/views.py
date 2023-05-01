from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        taskTitle = request.POST['title']
        taskDesc = request.POST['desc']
        ins = Task(taskTitle=taskTitle, taskDesc=taskDesc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def tasks(request):
    return render(request, 'tasks.html')
