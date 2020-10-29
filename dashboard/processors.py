from resume.forms import *
def updateForms(request):
    if request.user.is_authenticated:
        context =  {"profileForm":ProfileUpdateForm(instance=request.user.profile),
        "experienceForm":ExperienceUpdateForm(),
        "socialForm":SocialMediaUpdateForm(),
        "educationForm":EducationUpdateForm(),
        "skillForm":SkillUpdateForm(),
        "workFlow":WorkFlowUpdateForm(),
        "interestFlow":InterestUpdateForm(),
        "userForm":UserUpdateForm(instance=request.user),}
    else:
        context={}
    return context