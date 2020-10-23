from django.urls import re_path
from . import views
app_name = "app_resume"
urlpatterns = [
    re_path("^(?P<pk>\w*)/?$",views.ResumeHomeView.as_view(),name="resume_home"),
]
