from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('testimonial/', views.testimonial, name='testimonial'),
    
]
