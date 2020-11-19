from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import (CreateView,View,UpdateView,DeleteView)
from django.contrib.auth import authenticate,login,models
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
import random
from blog.models import BlogPost
from django.core.paginator import Paginator
from resume.models import (SocialMedia,Experience,Education,WorkFlow,Skill,Interest)
from resume.forms import (UserUpdateForm,ProfileUpdateForm,
SocialMediaUpdateForm,ExperienceUpdateForm,EducationUpdateForm,SkillUpdateForm,WorkFlowUpdateForm,
InterestUpdateForm)
class DashboardHomeView(LoginRequiredMixin,View):
    template_name="dashboard/home.html"
    def get(self,request):
        return render(request,"dashboard/home.html",)
    def post(self,request):
        action = request.POST.get("action",None)
        id = request.POST.get("pk",None)
        user = request.user
        if action:
            try:
                if action=="social":
                    social = SocialMedia.objects.get(id=id)
                    if user == social.user:
                        social.delete()
                    else:
                        messages.warning(request,"Unauthorized Action",fail_silently=True)
                elif action=="experience":
                    experience = Experience.objects.get(id=id)
                    if user == experience.user:
                        experience.user
                    else:
                        messages.warning(request,"Unauthorized Action",fail_silently=True)
                elif action=="education":
                    education = Education.objects.get(id=id)
                    if user == education.user:
                        education.delete()
                    else:
                        messages.warning(request,"Unauthorized Action",fail_silently=True)
                elif action == "workflow":
                    workflow = WorkFlow.objects.get(id=id)
                    if user == workflow.user:
                        workflow.delete()
                    else:
                        messages.warning(request,"Unauthorized Action",fail_silently=True)
                elif action == "skill":
                    skill = Skill.objects.get(id=id)
                    if user == skill.user:
                        skill.delete()
                    else:
                        messages.warning(request,"Unauthorized Action",fail_silently=True)
                elif action == "interest":
                    interest = Interest.objects.get(id=id)
                    if user == interest.user:
                        interest.get(id=id).delete()
                    else:
                        messages.warning(request,"Unauthorized Action",fail_silently=True)
                else:
                    messages.warning(request,"Deletion unsuccessful",fail_silently=True)
                    return HttpResponseRedirect(reverse("app_dashboard:dashboard_home"))
                if len(messages.get_messages(request))==0:
                    messages.success(request,"Deletion Successful",fail_silently=True)
            except:
                messages.warning(request,"Deletion unsuccessful",fail_silently=True)
        else:
            profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
            user_form = UserUpdateForm(request.POST,instance=request.user)
            social_form = SocialMediaUpdateForm(request.POST)
            experience_form = ExperienceUpdateForm(request.POST)
            education_form = EducationUpdateForm(request.POST)
            skill_form = SkillUpdateForm(request.POST)
            workflow_form = WorkFlowUpdateForm(request.POST)
            interest_form = InterestUpdateForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request,f"Updated Successfully ",fail_silently=True)
            elif social_form.is_valid():
                social = social_form.save(commit=False)
                social.user = request.user
                social.save()
                messages.success(request,f"Added Successfully ",fail_silently=True)
            elif experience_form.is_valid():
                experience = experience_form.save(commit=False)
                experience.user= request.user
                experience.save()
                messages.success(request,f"Added Successfully ",fail_silently=True)
            elif education_form.is_valid():
                education = education_form.save(commit=False)
                education.user=request.user
                education.save()
                messages.success(request,f"Added Successfully ",fail_silently=True)
            elif skill_form.is_valid():
                skill = skill_form.save(commit=False)
                skill.user = request.user
                skill.save()
                messages.success(request,f"Added Successfully ",fail_silently=True)
            elif workflow_form.is_valid():
                workflow = workflow_form.save(commit=False)
                workflow.user = request.user
                workflow.save()
                messages.success(request,f"Added Successfully ",fail_silently=True)
            elif interest_form.is_valid():
                interest = interest_form.save(commit=False)
                interest.user = request.user
                interest.save()
                messages.success(request,f"Added Successfully ",fail_silently=True)
            elif len(messages.get_messages(request))==0:
                messages.warning(request,f"Error Occured Try Again",fail_silently=True)
        return HttpResponseRedirect(reverse("app_dashboard:dashboard_home"))
class DashboardBlogs(LoginRequiredMixin,View):
    def get(self,request):
        blogs = request.user.author_blog.all()
        if blogs:
            paginator = Paginator(blogs,5)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            context = {
                "blogs":page_obj,
            }
        else:
            context={
                "blogs":"",
            }
        return render(request,"dashboard/list_blog.html",context)
    def post(self,request):
        blogs = BlogPost.objects.filter(title__contains=request.POST.get("query"))
        if blogs:
            paginator = Paginator(blogs,5)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            context = {
                "blogs":page_obj,
            }
        else:
            context={
                "blogs":"",
            }
        return render(request,"dashboard/list_blog.html",context)
class DashboardBlogUpdate(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = BlogPost
    fields = ["title","thumbnail","description",]
    template_name = "dashboard/detail_blog.html"
    def test_func(self):
        return self.get_object().author == self.request.user
    def handle_no_permission(self):
        messages.warning(self.request,"You're Unauthorized")
        return HttpResponseRedirect(reverse("app_dashboard:dashboard_home"))
    def form_valid(self,form):
        return super(DashboardBlogUpdate,self).form_valid(form)
    def get_success_message(self,cleaned_data):
        self.success_message = f"{self.get_object().title} has been modified"
        return super().get_success_message(cleaned_data)
class DashboardBlogAdd(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = BlogPost
    fields = ["title","thumbnail","description",]
    template_name = "dashboard/add_blog.html"
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super(DashboardBlogAdd,self).form_valid(form)
    def get_success_message(self,cleaned_data):
        self.success_message = f"{cleaned_data.get('title')} has been added"
        return super().get_success_message(cleaned_data)
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
def dashboardDelete(request,model,pk):
    if request.method=="POST":
        if model=="social":
            SocialMedia.objects.get(id=pk).delete()
            messages.success(request,"Deletion Successful",fail_silently=True)
    return render(request,"dashboard/home.html")