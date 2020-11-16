from django.contrib import admin
from .models import BlogPost,ProfileLog,Comment
# Register your models here.
class AdminBlog(admin.ModelAdmin):
    list_display = ("author","title","created_on",)
    search_fields = ("author","title",)
class AdminComment(admin.ModelAdmin):
    list_display = ("comment","user","post")
    search_fields = ("comment","user","post")
admin.site.register(BlogPost,AdminBlog)
admin.site.register(ProfileLog)
admin.site.register(Comment,AdminComment)