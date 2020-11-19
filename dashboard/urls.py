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
    path("blogs/",views.DashboardBlogs.as_view(),name="dashboard_blogs"),
    path("update/<int:pk>/",views.DashboardBlogUpdate.as_view(),name="dashboard_blog_update"),
    path("blog/add/",views.DashboardBlogAdd.as_view(),name="dashboard_blog_add"),
    path("",views.DashboardHomeView.as_view(),name="dashboard_home"),
]
