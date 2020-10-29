from .models import (Profile,Experience,SocialMedia,
Education,Skill,WorkFlow,Interest)
from django.contrib.auth.models import User
from django import forms
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user",]
class AbsUpdateForm(forms.ModelForm):
    class Meta:
        exclude = ["user",]
class ExperienceUpdateForm(AbsUpdateForm):
    class Meta(AbsUpdateForm.Meta):
        model = Experience
class SocialMediaUpdateForm(AbsUpdateForm):
    class Meta(AbsUpdateForm.Meta):
        model = SocialMedia
class EducationUpdateForm(AbsUpdateForm):
    class Meta(AbsUpdateForm.Meta):
        model =Education
class SkillUpdateForm(AbsUpdateForm):
    class Meta(AbsUpdateForm.Meta):
        model = Skill
class WorkFlowUpdateForm(AbsUpdateForm):
    class Meta(AbsUpdateForm.Meta):
        model = WorkFlow
class InterestUpdateForm(AbsUpdateForm):
    class Meta(AbsUpdateForm.Meta):
        model = Interest
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name"]