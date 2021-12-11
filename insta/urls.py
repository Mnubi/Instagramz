from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name = 'index'),
    path('search/', views.search, name='search'),
    path('profile',views.show_profile, name='profile'),
    path('posts/',views.new_post, name='post'),
    path('comment/<id>', views.comment, name='comment'),
    path('post/<int:image_id>/like', views.like_image, name='like_image'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('accounts/profile/',views.show_profile, name='profile'),
]