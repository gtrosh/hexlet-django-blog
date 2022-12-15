# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    app_name = 'article'
    return render(request, 'index.html', context={'article': app_name})
