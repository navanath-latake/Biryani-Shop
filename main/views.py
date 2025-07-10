from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def base(request):
    return render(request, 'base.html')