from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import (CreateView,View,TemplateView)
from django.contrib.auth import authenticate,login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
import random
class DashboardHomeView(LoginRequiredMixin,TemplateView):
    template_name="dashboard/home.html"
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