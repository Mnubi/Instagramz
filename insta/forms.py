from .models import Image
from django.forms import ModelForm
from django import forms
from django import forms
from .models import Comment, Image, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewPostForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',
                  'img_name',
                  'caption',)



class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'email')

class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes','comments']

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment'

    class Meta:
        model = Comment
        fields = ('comment',)