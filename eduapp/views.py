from django.shortcuts import render, get_object_or_404

def index(request):

    context = {}

    return render(request, 'index.html', context)

def course_view(request):

    context = {}

    return render(request, 'courses.html', context)

def single_course_view(request):

    context = {}

    return render(request, 'single-courses.html', context)