from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.paginator import Paginator
from .models import BlogPost,Comment
from .forms import CommentForm
from django.contrib import messages
import copy
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404
from django.conf import settings
# Create your views here.
class BlogsList(View):
    def get(self,request):
        if request.GET.get("query"):
            blogs = BlogPost.objects.filter(title__contains=request.GET.get("query"))|BlogPost.objects.filter(author__username=request.GET.get("query"))
        else:
            blogs = BlogPost.objects.all()
        if blogs:
            paginator = Paginator(blogs,8)
            page_number = request.GET.get("page")
            blogs = paginator.get_page(page_number)
        context = {
            "blogs":blogs,
        }
        return render(request,"blog/home.html",context)
class BlogDetail(DetailView):
    model = BlogPost
    template_name = "blog/detail_blog.html"
    context_object_name = "blog"
    def get(self,request,*args,**kwargs):
        if request.GET.get("comment"):
            request_GET_copy = copy.copy(request.GET)
            request_GET_copy["post"] = self.get_object()
            if self.request.user.is_authenticated:
                request_GET_copy["user"] = self.request.user
            comment_form = CommentForm(request_GET_copy)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(self.request,"Comment Added Successfully",fail_silently=True)
                return HttpResponseRedirect(reverse("app_blog:blog_detail",args=(self.get_object().slug,)))
        return super().get(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        comments = self.get_object().blog_comment.all()
        paginator = Paginator(comments,4)
        page_number = self.request.GET.get("page")
        on_page_comments = paginator.get_page(page_number)
        context["comments"] =  on_page_comments
        self.object.views +=1
        self.object.save(update_fields=["views",])
        return context