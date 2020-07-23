from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "internationaleregler/home.html")


def drengene(request):
    return render(request, "internationaleregler/drengene.html")