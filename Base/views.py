import os
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect

from portfolio import settings
from .models import About, Skill, Education, Project, Message
from math import ceil
from django.contrib.auth import authenticate, login
from django.contrib import messages


from django.db.models import F

def get_context():
    """Helper function to generate context for rendering the home page."""
    about = About.objects.first()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    for education in educations:
        education.duration = ceil((education.end_date - education.start_date).days / 30)
    projects = Project.objects.all()

    # Fetch messages ordered by date (latest first)
    my_messages = Message.objects.all().order_by('-date')  # Assuming 'date' is the field storing message timestamp

    # Group projects into chunks of 3
    project_chunks = [projects[i:i+3] for i in range(0, len(projects), 3)]

    return {
        'about': about,
        'skills': skills,
        'educations': educations,
        'project_chunks': project_chunks,
        'my_messages': my_messages,
        'projects': projects,
    }


def home(request):
    context = get_context()
    return render(request, 'home.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('name', '').strip()
        password = request.POST.get('password', '').strip()

        context = get_context()
        if not username or not password:
            messages.error(request, 'Username and password are required.', extra_tags='login')
            context['show_login_modal'] = True
            return render(request, 'home.html', context)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials.',extra_tags='login')
            context['show_login_modal'] = True
            return render(request, 'home.html', context)

    return redirect('/')

def leave_message(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        context = get_context()
        try:
            Message.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, f'Thank you for sending your message, {name}.', extra_tags='leave_message')
            context['show_newMessage_modal'] = True
            return render(request, 'home.html', context)
        except Exception as e:
            messages.error(request, 'sorry try again later', extra_tags='leave_message')
            context['show_newMessage_modal'] = True
            return render(request, 'home.html', context)

        
    return redirect('/')

# CRUD operations
#Skills
def update_skill(request, pk):
    obj = Skill.objects.get(pk=pk)
    obj.name = request.POST.get('name')
    obj.level = request.POST.get('level')

    context = get_context()

    if 'image' in request.FILES:
        obj.image = request.FILES['image']
    obj.save()
    messages.success(request, f'{obj.name} updated', extra_tags='leave_message')
    context['show_newMessage_modal'] = True

    return render(request, 'home.html', context)

def delete_skill(request, pk):
    obj = Skill.objects.get(pk=pk)
    skill_name = obj.name
    obj.delete()
    context = get_context()

    messages.success(request, f'{obj.name} deleted', extra_tags='leave_message')
    context['show_newMessage_modal'] = True

    return render(request, 'home.html', context)

def create_skill(request):
    context = get_context()
    try:
        name = request.POST.get('name')
        level = request.POST.get('level')
        if 'image' in request.FILES:
            obj = Skill.objects.create(
                name=name,
                level=level,
                image = request.FILES['image']
            )
        messages.success(request,f'{name}created successfully', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request,'home.html', context)
    except Exception as e:
        messages.error(request,f'try again later \n {e}', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request,'home.html', context)
        
def update_project(request, pk):
    obj = Project.objects.get(pk=pk)
    obj.name = request.POST.get('name')
    obj.description = request.POST.get('description')
    obj.link = request.POST.get('link')

    if 'image' in request.FILES:
        obj.image = request.FILES['image']
        print('found image')

    obj.save()
    context = get_context()
    messages.success(request,f'{obj.name} updated successfully', extra_tags='leave_message')
    context['show_newMessage_modal'] = True
    return render(request, 'home.html', context)

def delete_project(request, pk):
    obj = Project.objects.get(pk=pk)
    project = obj.name
    obj.delete()
    context = get_context()

    messages.success(request, f'{project} deleted successfully', extra_tags='leave_message')
    context['show_newMessage_modal'] = True
    return render(request, 'home.html', context)

def create_project(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    link = request.POST.get('link')
    context = get_context()

    try:
        if 'image' in request.FILES:
            Project.objects.create(
                name = name,
                description = description,
                link = link,
                image = request.FILES['image']
            )
        else:
            messages.error(request, 'please provide image', extra_tags='leave_message')
            context['show_newMessage_modal'] = True
            return render(request, 'home.html', context) 
        
        messages.success(request, f'{name} created successfully', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request, 'home.html', context)
    except Exception as e:
        messages.error(request, f'failed coz {e}', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request, 'home.html', context)

def edit_me(request):
    obj = About.objects.first()
    obj.name = request.POST.get('name')
    obj.surname = request.POST.get('surname')
    obj.age = request.POST.get('age')
    obj.story = request.POST.get('story')

    if 'image' in request.FILES:
        obj.image = request.FILES['image']
        print('image found')
    obj.save()
    messages.success(request, f'{obj.name}. Your profile has been updated successfully', extra_tags='leave_message')
    context = get_context()
    context['show_newMessage_modal'] = True
    return render(request, 'home.html', context)

def edit_education(request, pk):
    obj = Education.objects.get(pk=pk)
    name = request.POST.get('name')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    
    obj.name = name
    if start_date != '':
        obj.start_date = start_date
    if end_date != '':
        obj.end_date = end_date
    if 'image' in request.FILES:
        obj.image = request.FILES['image']

    obj.save()
    messages.success(request, f'{obj.name} updated successfully', extra_tags='leave_message')
    context = get_context()
    context['show_newMessage_modal'] = True
    return render(request, 'home.html', context)

def delete_education(request, pk):
    obj = Education.objects.get(pk=pk)
    name = obj.name
    obj.delete()
    messages.success(request, f'{name} deleted successfully', extra_tags='leave_message')
    context = get_context()
    context['show_newMessage_modal'] = True
    return render(request, 'home.html', context)

def create_education(request):
    name = request.POST.get('name')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    img = ''
    context = get_context()

    if 'image' in request.FILES:
        img = request.FILES['image']

    if start_date == '' or end_date == '' or img == '':
        messages.error(request, 'please provide all details', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request, 'home.html', context)
    try:
        Education.objects.create(
            name = name,
            start_date = start_date,
            end_date = end_date,
            image = img
        )
        messages.success(request, f'{name} created successfully', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request, 'home.html', context)
    except Exception as e:
        messages.error(request, f'Oops, {e}', extra_tags='leave_message')
        context['show_newMessage_modal'] = True
        return render(request, 'home.html', context)


def serve_cv(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv', file_name)
    
    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
    else:
        # Return a 404 if the file is not found
        return HttpResponse("File not found", status=404)