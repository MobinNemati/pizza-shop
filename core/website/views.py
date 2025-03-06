from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, DeleteView
from menu.models import Item, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Contact, Employee


    

class IndexView(TemplateView):
    template_name = 'website/index.html'




class ServicesView(TemplateView):
    template_name = 'website/services.html'




class BlogView(TemplateView):
    template_name = 'website/blog.html'




class AboutView(ListView):
    model = Employee
    template_name = "website/about.html"
    context_object_name = 'employees'


    def get_queryset(self):
        return Employee.objects.all()

    




class BlogSingleView(TemplateView):
    template_name = "website/blog.html"




class ContactView(CreateView):
    model = Contact
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        messages.success(self.request, "Your message has been successfully sent!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your submission.")
        return super().form_invalid(form)








