from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from pathlib import Path
import re
from PIL import Image
def validate_num(value):
    num_pattern = re.compile(r"""
    ^(\+)?          
    (\d{1,3})?          #Country Code
    (-)?                #Separator
    (\d{3})             #area code
    (-)?                #Separator
    (\d{3})             #first 3 digits
    (-)?                #Separator
    (\d{4})$            #last 4 digits
    """,re.VERBOSE)
    mo = num_pattern.findall(str(value))
    if not mo:
        raise ValidationError(
            f"{value} is an invalid number.Format:AAA-BBB-CCCC"
        )
GENDER_CHOICES = (
    ("male","MALE"),
    ("female","FEMALE"),
    ("other","OTHER"),
)
SOCIAL_MEDIA_CHOICES = (
    ("github","GITHUB"),
    ("facebook","FACEBOOK"),
    ("youtube","YOUTUBE"),
    ("instagram","INSTAGRAM"),
    ("linkedin","LINKEDIN"),
    ("twitter","TWITTER"),
    ("website","WEBSITE")
)
def resize_image(image_src,image_size):
    org_img = Image.open(image_src)
    if org_img.width > image_size[0] or org_img.height >image_size[1]:
        org_img.thumbnail((image_size[0],image_size[1]))
        org_img.save(image_src)
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    resume_pic = models.ImageField(default="profile_pics/default.png",upload_to="profile_pics")
    profile_pic = models.ImageField(default="profile_pics/profiledefault.png",upload_to="profile_pics")
    favicon = models.ImageField(default="profile_pics/favicondefault.png",upload_to="profile_pics")
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default="male")
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact_num = models.CharField(max_length=17,validators=[validate_num,])
    show_num = models.BooleanField(default=False)
    def save(self,*args, **kwargs):
        super().save(*args,**kwargs)
        if not (self._meta.get_field("profile_pic").default in self.profile_pic.path):
            resize_image(self.profile_pic.path,(60,60))
        if not (self._meta.get_field("resume_pic").default in self.resume_pic.path):
            resize_image(self.resume_pic.path,(500,500))
        if not (self._meta.get_field("favicon").default in self.favicon.path):
            resize_image(self.favicon.path,(16,16))
class SocialMedia(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_social")
    platform = models.CharField(choices=SOCIAL_MEDIA_CHOICES,max_length=9,default="facebook")
    url = models.URLField()
    def __str__(self):
        return f"{self.user}'s {self.platform}"
    class Meta:
        verbose_name_plural = "Social Media"
class AbsModel(models.Model):
    organization = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True,blank=True)
    class Meta:
        ordering=["-start_date"]
        abstract=True
class Experience(AbsModel):
    user = user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_experience")
    position = models.CharField(max_length=40)
class Education(AbsModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_education")
    faculty = models.CharField(max_length=50)
class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_skill")
    language_tool = models.CharField(max_length=20)
class WorkFlow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_workflow")
    workflow  = models.CharField(max_length=50)
class Interest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_interest")
    description = AbsModel._meta.get_field("description") #gets description field from AbsModel