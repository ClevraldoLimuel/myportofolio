from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")

def interest_page(request):
    return render(request, "interest.html")