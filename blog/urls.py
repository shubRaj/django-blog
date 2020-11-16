from django.urls import path
from . import views
app_name = "app_blog"
urlpatterns = [
    path("",views.BlogsList.as_view(),name="blog_lists"),
    path("<slug:slug>/",views.BlogDetail.as_view(),name="blog_detail"),
]
