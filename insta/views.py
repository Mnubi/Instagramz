from django.forms.fields import ImageField
from django.shortcuts import render, redirect
from django.http  import HttpResponse, HttpResponseRedirect

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Instagram Replica')


  
from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponse
from insta.models import Comment, Image, Profile
from .forms import CommentForm, NewPostForm, UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

# @login_required(login_url='/accounts/login/')
def homepage(request):
    """
    View function to display homepage content
    """
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()

    return render(request, 'index.html',{"posts":posts,"profile":profile,"comment":comment})

# @login_required(login_url='/registration/login/')    
def show_profile(request):
    current_user= request.user
    images= Image.objects.filter(profile=current_user.id).all
    profile = Profile.objects.filter(user_id=current_user.id).first()

    return render(request, 'registration/profile.html',{"images":images, "profile":profile} )

# @login_required(login_url='/accounts/login/')    
# def update_profile(request,id):
    
#     obj = get_object_or_404(Profile,user_id=id)
#     obj2 = get_object_or_404(User,id=id)
#     form = UpdateProfileForm(request.POST or None, instance = obj)
#     form2 = UpdateUserForm(request.POST or None, instance = obj2)
#     if form.is_valid() and form2.is_valid():
#         form.save()
#         form2.save()
#         return HttpResponseRedirect("/profile")
    
#     return render(request, "registration/update_profile.html", {"form":form, "form2":form2})


# @login_required(login_url='/accounts/login/')
def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")

        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'search.html',{'profiles': results,'message': message})
    else:
        message = "You haven't entered anything to search. Please enter a user profile to search."
    return render(request, 'search.html', {'message': message})

# @login_required(login_url='/accounts/login/')
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.save(commit=False)
            image.save()
        return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

# @login_required(login_url='/accounts/login/')
def comment(request,id):
    post_comment = Comment.objects.filter(post= id)
    image = Image.objects.filter(id=id).first()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = current_user
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request,'comment.html',{"form":form,"img":image,"comments":post_comment})

#@login_required(login_url='/accounts/login/')
def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Image.objects.get(id=image_id)
        if user in image_pic.like_count.all():
            image_pic.like_count.add(user)
        else:
            image_pic.like_count.add(user)
        like,created =Like.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'
        like.save()
    return redirect('/')