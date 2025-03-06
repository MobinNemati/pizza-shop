from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from accounts.models import Profile
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from accounts.forms import SignUpForm
from django.views import View






class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(phone_number=self.request.user)
    
    

class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(phone_number=user.phone_number, password=request.POST["password"])
            if user:
                login(request, user)
                return redirect('/accounts/profile')

        return render(request, 'registration/signup.html', {'form': form})



