from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="thumbnail",default="thumbnail/default.png")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="author_blog")
    slug = models.SlugField(unique=True,blank=True)
    views = models.IntegerField(default=0)
    def save(self,*args,**kwargs):
        self.slug = slugify(f"{self.title} {self.author}")
        self.last_updated = timezone.now()
        super(BlogPost,self).save(*args,**kwargs)
    class Meta:
        verbose_name="Blog"
        ordering = ["-created_on",]
    def get_absolute_url(self):
        return reverse("app_dashboard:dashboard_blogs")