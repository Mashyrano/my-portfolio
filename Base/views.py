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

    # Group projects into chunks of 3
    project_chunks = [projects[i:i+3] for i in range(0, len(projects), 3)]

    return render(request, 'home.html', {
        'about': about,
        'skills': skills,
        'educations': educations,
        'project_chunks': project_chunks,
    })
