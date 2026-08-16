from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет! Это главная страница.")
    # или render(request, 'home.html') если используешь шаблоны
