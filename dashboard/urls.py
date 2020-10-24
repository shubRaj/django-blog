from django.urls import path
from . import views
app_name = "app_dashboard"
urlpatterns = [
    path("login/",views.DashboardLoginView.as_view(),name="dashboard_login"),
    path("signup/",views.DashboardRegisterView.as_view(),name="dashboard_signup"),
    path("logout/",views.DashboardLogoutView.as_view(),name="dashboard_logout"),
    path("",views.DashboardHomeView.as_view(),name="dashboard_home"),
]
