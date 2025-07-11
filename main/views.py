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

def mutton(request):
    return render(request, 'subPages/mutton.html')

def chicken(request):
    return render(request, 'subPages/chicken.html')

def egg(request):
    return render(request, 'subPages/egg.html')

def fish(request):
    return render(request, 'subPages/fish.html')

def fry(request):
    return render(request, 'subPages/fry.html')

def raita(request):
    return render(request, 'subPages/raita.html')

def sweet(request):
    return render(request, 'subPages/sweet.html')