from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Interest, Education, Project
from main.forms import ProjectForm


def show_main(request):
    context = {
        "name": "Clevraldo Limuel",
        "name_short": "Clevr",
        "npm": "2506656583",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia. Aiming to be a better person. Currently learning much"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Clevraldo Limuel",
        "name_short": "Clevr",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_interest(request):
    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "technologies": Interest.objects.filter(category="technology"),
        "creatives": Interest.objects.filter(category="creative"),
        "leisures": Interest.objects.filter(category="leisure"),
    }
    return render(request, "interest.html", context)

def show_education(request):
    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "education_history": Education.objects.all().order_by('admission_year')
    }
    return render(request, "education.html", context)

def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "form": form,
    }
    return render(request, "project_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")