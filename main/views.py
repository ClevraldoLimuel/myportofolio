from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied      
import datetime


from main.models import Experience, Interest, Education, Project
from main.forms import ProjectForm, InterestForm

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Clevraldo Limuel",
        "name_short": "Clevr",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Clevraldo Limuel",
        "name_short": "Clevr",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Clevraldo Limuel",
        "name_short": "Clevr",
        "npm": "2506656583",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia. Aiming to be a better person. Currently learning much"
        ),
        "last_login": last_login,
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
    name_query = request.GET.get("name", "").strip()
    json_response = get_interest_json(request)
    interests = serializers.deserialize("json", json_response.content.decode("utf-8"))
    
    interests = [ item.object for item in interests ]
    
    technologies = [ interest for interest in interests if interest.category == "technology" ]
    creatives = [ interest for interest in interests if interest.category == "creative" ]
    leisures = [ interest for interest in interests if interest.category == "leisure" ]
    
    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "technologies": technologies,
        "creatives": creatives,
        "leisures": leisures,
        "name_query": name_query,
    }
    
    for interest in interests:
        interest.edit_form = InterestForm(instance=interest)

    return render(request, "interest.html", context)

@login_required(login_url="/login/")
def create_interest(request):
    if not request.user.is_superuser:
            raise PermissionDenied
    form = InterestForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "Peminatan baru berhasil ditambahkan!")
            return redirect("main:show_interest")
    
    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "form": form,
    }
    
    return render(request, "interest_form.html", context)

@login_required(login_url="/login/")
def delete_interest(request, interest_id):
    if not request.user.is_superuser:
            raise PermissionDenied    
    interest = get_object_or_404(Interest, pk=interest_id)
    print("DELETE VIEW REACHED!", interest_id, request.method, flush=True)

    if request.method == "POST":
        interest.delete()
        messages.success(request, "Minat berhasil dihapus!")
        return redirect("main:show_interest")

    return redirect("main:show_interest")

def get_interest_json(request):
    name_query = request.GET.get("name", "").strip()
    interests = Interest.objects.all()

    if name_query:
        interests = interests.filter(name__icontains=name_query)

    interests_json = serializers.serialize("json", interests, use_natural_foreign_keys=True)
    return HttpResponse(interests_json, content_type="application/json")

@login_required(login_url="/login/")
def edit_interest(request, interest_id):
    if not (request.user.is_superuser or request.user.has_perm("main.change_interest")):
            raise PermissionDenied
    interest = get_object_or_404(Interest, pk=interest_id)
    
    if request.method == "POST":
        form = InterestForm(request.POST, instance=interest)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Minat berhasil diedit!")
            return redirect("main:show_interest")
    else:
        form = InterestForm(instance=interest)
    
    context = {
        "form": form,
        "interest": interest        
    }
    return render(request, "interest_edit_modal.html", context)

@login_required(login_url="/login/")
def toggle_star_interest(request, interest_id):
    interest = get_object_or_404(Interest, pk=interest_id)

    if request.method == "POST":
        if request.user in interest.starred_by.all():
            interest.starred_by.remove(request.user)
        else:
            interest.starred_by.add(request.user)

    return redirect("main:show_interest")

def show_education(request):
    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "education_history": Education.objects.all().order_by('admission_year')
    }
    return render(request, "education.html", context)

def show_project(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name":"Clevraldo Limuel",
        "name_short": "Clevr",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

from django.views.decorators.http import require_POST

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)