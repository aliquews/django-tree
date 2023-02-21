from django.shortcuts import render


def index(request, name):
    return render(request, 'index.html', context={'name': name})