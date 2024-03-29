from django.forms.fields import ImageField
from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponse
from insta.models import Comment, Image, Like, Profile
from .forms import CommentForm, NewPostForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Instagram Replica')


# from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

@login_required(login_url='/accounts/login/')
def homepage(request):
    """
    View function to display homepage content
    """
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()

    return render(request, 'index.html',{"posts":posts,"profile":profile,"comment":comment})

@login_required(login_url='/registration/login/')    
def show_profile(request):
    current_user= request.user
    images= Image.objects.filter(profile=current_user.id).all
    profile = Profile.objects.filter(user_id=current_user.id).first()

    return render(request, 'registration/profile.html',{"images":images, "profile":profile} )

@login_required(login_url='/accounts/login/')    
def update_profile(request):
    current_user= request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    form=UpdateProfileForm()
    if request.method=='POST':
        form=UpdateProfileForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            redirect("/profile")
    
    return render(request, "registration/update_profile.html", {"form":form, "profile":profile})


@login_required(login_url='/accounts/login/')
def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")

        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'search.html',{'profiles': results,'message': message})
    else:
        message = "You haven't entered anything to search. Please enter a user profile to search."
    return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login/')
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.save(commit=False)
            image.profile=request.user
            if 'img' in request.FILES:
                image.image=request.FILES['img']
            image.save()
        return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def like_image(request, image_id):
    image = get_object_or_404(Image,id = image_id)
    like = Like.objects.filter(image = image ,user = request.user).first()
    if like is None:
        like = Like()
        like.image = image
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('index')