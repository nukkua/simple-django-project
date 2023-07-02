from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from django.shortcuts import get_object_or_404, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = "Django Course!!!"
    return render(request, "index.html", {"title": title})


def about(request):
    username = {"name": "leverna"}
    return render(request, "about.html", {"username": username})


def hello(request, username):
    return HttpResponse(f"<h2>Hello {username} !!</h2>")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})
    # return JsonResponse(projects ,safe=False)


def tasks(request):
    # task = get_object_or_404(Tasks, title=title)
    tasks = Tasks.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})
    # return HttpResponse(f'task : {task.title}')


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": CreateNewTask})
    else:
        Tasks.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(
            request, "projects/create_project.html", {"form": CreateNewProject()}
        )
    else:
        project = Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id = id)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })