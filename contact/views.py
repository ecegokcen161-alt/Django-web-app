from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': 'home'})


def contact(request):
    return render(request, 'contact.html', {'title': 'contact'})