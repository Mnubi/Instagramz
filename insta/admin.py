from django.contrib import admin
from .models import Comment, Image, Like,Profile

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Comment)