from django.shortcuts import render, redirect
from .models import (
    Profile,
    Experience,
    Project,
    Education,
    Interest,
    SkillCategory,
    Language,
    AwsBadge,
    Certificate,
    ContactMessage,
)


def index(request):
    context = {
        'title': 'home',
        'profile': Profile.objects.first(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'education': Education.objects.first(),
        'interests': Interest.objects.all(),
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all(),
        'languages': Language.objects.all(),
        'aws_badges': AwsBadge.objects.all(),
        'certificates': Certificate.objects.all(),
    }

    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        return redirect('contact')

    return render(request, 'contact.html', {'title': 'contact'})