from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name = 'index'),
    path('search/', views.search, name='search'),
    path('profile',views.show_profile, name='profile'),
    path('posts/',views.new_post, name='post'),
    path('comment/<id>', views.comment, name='comment'),
    path('accounts/profile/',views.show_profile, name='profile'),
]