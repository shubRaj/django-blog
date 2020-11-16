from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="thumbnail",default="thumbnail/default.png")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="author_blog")
    slug = models.SlugField(unique=True,blank=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug = slugify(f"{self.title} {self.author}")
        self.last_updated = timezone.now()
        super(BlogPost,self).save(*args,**kwargs)
    class Meta:
        verbose_name="Blog"
        ordering = ["-created_on",]
    def get_absolute_url(self):
        return reverse("app_dashboard:dashboard_blogs")
class Abslog(models.Model):
    ip_address = models.CharField(max_length=18,blank=True,null=True)
    user_agent = models.CharField(max_length=283,blank=True,null=True)
    country = models.CharField(max_length=30,blank=True,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    timestamp = models.TimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.ip_address}"
    
    class Meta:
        ordering=["-timestamp"]
        abstract=True
class ProfileLog(Abslog):
   user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_log",blank=True,null=True)
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_comment",null=True,blank=True)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name="blog_comment",null=True,blank=True)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.comment
    class Meta:
        ordering=["-created_on"]
    