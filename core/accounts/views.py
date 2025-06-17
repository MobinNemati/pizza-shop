from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from accounts.models import Profile
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from accounts.forms import SignUpForm, LoginForm
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



class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        return render(request, 'registration/login.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('/accounts/profile')
            else:
                messages.error(request, 'Invalid username or password')


        return render(request, 'registration/login.html', {'form': form})

    
class LogoutView(View, LoginRequiredMixin):

    def get(self, request):
        logout(request)
        return redirect('/')
