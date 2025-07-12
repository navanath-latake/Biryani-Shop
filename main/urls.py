from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('mutton/', views.mutton, name='mutton'),
    path('chicken/', views.chicken, name='chicken'),
    path('egg/', views.egg, name='egg'),
    path('fish/', views.fish, name='fish'),
    path('fry/', views.fry, name='fry'),
    path('raita/', views.raita, name='raita'),
    path('sweet/', views.sweet, name='sweet')
    
]
