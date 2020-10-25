from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import DetailView,TemplateView,View
class ResumeHomeView(View):
    template_name = "resume/home.html"
    def get(self,request,**kwargs):
        user_name = kwargs.get("pk")
        try:
            whois = User.objects.get(username=user_name)
        except User.DoesNotExist:
            whois = User.objects.all().first()
        return render(request,self.template_name,{"whois":whois})