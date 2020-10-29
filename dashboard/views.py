from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import (CreateView,View,UpdateView,DeleteView)
from django.contrib.auth import authenticate,login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
import random
from resume.models import SocialMedia
from resume.forms import UserUpdateForm,ProfileUpdateForm,SocialMediaUpdateForm
class DashboardHomeView(LoginRequiredMixin,View):
    template_name="dashboard/home.html"
    def get(self,request):
        return render(request,"dashboard/home.html")
    def post(self,request):
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        user_form = UserUpdateForm(request.POST,instance=request.user)
        social_form = SocialMediaUpdateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f"Updated Successfully ",fail_silently=True)
        if social_form.is_valid():
            social = social_form.save(commit=False)
            social.user = request.user
            social.save()
            messages.success(request,f"Added Successfully ",fail_silently=True)
        return HttpResponseRedirect(reverse("app_dashboard:dashboard_home"))
class DashboardLoginView(UserPassesTestMixin,SuccessMessageMixin,LoginView):
    template_name = "dashboard/login.html"
    success_login_messages=["Welcome back! %s .This place hasn't been the same without you",
    "So Glad You're Back,%s","Welcome back! %s .There will be forcefull resistance if you ever try to leave again",]
    def get_success_url(self):
        return reverse("app_dashboard:dashboard_home")
    def get_success_message(self,cleaned_data):
        self.success_message = random.choice(self.success_login_messages)%(self.request.user.get_full_name())
        return super().get_success_message(cleaned_data)
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("app_dashboard:dashboard_home"))
class DashboardLogoutView(LoginRequiredMixin,LogoutView):
    template_name = "dashboard/logout.html"
class DashboardRegisterView(UserPassesTestMixin,SuccessMessageMixin,CreateView):
    form_class = UserRegistrationForm
    template_name = "dashboard/register.html"
    def get_success_url(self):
        return reverse("app_dashboard:dashboard_home")
    def get_success_message(self,cleaned_data):
        self.success_message = f'Account for {cleaned_data.get("username")} has been created successfully.'
        return super().get_success_message(cleaned_data)
    def form_valid(self,form):
        saved_form = super().form_valid(form)
        username,password = form.cleaned_data.get("username"),form.cleaned_data.get("password1")
        user = authenticate(username=username,password=password)
        login(self.request,user)
        return saved_form
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("app_dashboard:dashboard_home"))
class DashboardDeleteSocialView(DeleteView):
    model = SocialMedia
    def get_success_url(self):
        return reverse("app_dashboard:dashboard_home")