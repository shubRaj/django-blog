from django.contrib import admin
from .models import (
Profile,SocialMedia,Education,Interest,Skill,Experience,WorkFlow)
class AdminProfile(admin.ModelAdmin):
    list_display = ("user","contact_num",)
    search_fields = ("contact_num","user__username","user__email")
class AdminSocialMedia(admin.ModelAdmin):
    list_display = ("user","platform","url")
admin.site.register(Profile,AdminProfile)
admin.site.register(SocialMedia,AdminSocialMedia)
myModels = [Education,Interest,Skill,Experience,WorkFlow]
class AdminAbstract(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user",)
admin.site.register(myModels,AdminAbstract)
# Register your models here.
