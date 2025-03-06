from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('single/', views.BlogSingleView.as_view(), name='blog-single'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contact/', views.ContactView.as_view(), name='contact'),


]

