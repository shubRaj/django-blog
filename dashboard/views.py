from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import (CreateView,View)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin

from django.urls import reverse
from .forms import UserRegistrationForm
class DashboardLoginView(UserPassesTestMixin,PermissionRequiredMixin,LoginView):
    template_name = "dashboard/login.html"
    redirect_field_name="/"
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect("/")
class DashboardLogoutView(LoginRequiredMixin,LogoutView):
    template_name = "dashboard/logout.html"
class DashboardRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "dashboard/register.html"
    success_url = "dashboard/"