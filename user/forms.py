from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileForm(UserCreationForm):
    class Meta:
        model=Profile
        fields=['username','email','password1','password2','city','respondent']




















