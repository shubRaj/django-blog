from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
app_name = "app_dashboard"
urlpatterns = [
    path("login/",views.DashboardLoginView.as_view(),name="dashboard_login"),
    path("signup/",views.DashboardRegisterView.as_view(),name="dashboard_signup"),
    path("logout/",views.DashboardLogoutView.as_view(),name="dashboard_logout"),
    path("profile/",login_required(TemplateView.as_view(template_name="dashboard/profile.html")),name="dashboard_profile"),
    path("deletesocial/<int:pk>",views.DashboardDeleteSocialView.as_view(),name="dashboard_deleteSocial"),
    path("",views.DashboardHomeView.as_view(),name="dashboard_home"),
]
