from django.shortcuts import render
from .models import About, Skill, Education, Project
from math import ceil

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    for education in educations:
        education.duration = ceil((education.end_date - education.start_date).days / 30)
    projects = Project.objects.all()

    return render(request, 'home.html', {
        'about': about,
        'skills': skills,
        'educations': educations,
        'projects': projects,
    })
