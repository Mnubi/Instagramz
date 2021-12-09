from django.shortcuts import render, redirect
from django.http  import HttpResponse, HttpResponseRedirect

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Instagram Replica')


  
from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponse
from insta.models import Comment, Image, Profile
from .forms import NewPostForm
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

# @login_required(login_url='/accounts/login/')    
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

        print(user)
        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'all-templates/search.html',{'profiles': results,'message': message})
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
    images = Image.objects.filter(id=id).all()
    current_user = request.user
    profile = request.GET.get("profile")
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request,'comment.html',{"form":form,"images":images,"comments":post_comment})