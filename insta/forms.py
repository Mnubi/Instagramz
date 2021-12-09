from .models import Image
from django.forms import ModelForm
from django import forms

class NewPostForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',
                  'img_name',
                  'caption',)