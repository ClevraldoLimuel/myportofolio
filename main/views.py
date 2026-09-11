from django.shortcuts import render

from main.models import Experience
from main.models import Interest


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