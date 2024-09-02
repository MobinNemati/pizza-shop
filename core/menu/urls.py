from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('blog/', views.blog.as_view(), name='blog'),
    path('about/', views.about, name='about'),
    path('single/', views.BlogSingle, name='blog-single'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('services/', views.services, name='services'),


]

