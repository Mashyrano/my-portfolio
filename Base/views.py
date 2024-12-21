from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import About, Skill, Education, Project
from math import ceil
from django.contrib.auth import authenticate, login
from django.contrib import messages


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


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('name', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'home.html', {'show_login_modal': True})

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'home.html', {'show_login_modal': True})

    return redirect('/')