from django.contrib import admin
from .models import BlogPost
# Register your models here.
class AdminBlog(admin.ModelAdmin):
    list_display = ("author","title","created_on",)
    search_fields = ("author","title",)
admin.site.register(BlogPost,AdminBlog)