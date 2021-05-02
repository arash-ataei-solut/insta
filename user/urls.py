from django.contrib.auth.views import LoginView
from django.urls import path

from user.views import UserListView, ProfileView, FollowView, UnfollowView, FollowingListView, FollowerListView, \
    RegistrationView

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('', UserListView.as_view(), name='user-list'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:pk>/', UnfollowView.as_view(), name='unfollow'),
    path('following/', FollowingListView.as_view(), name='following'),
    path('follower/', FollowerListView.as_view(), name='follower'),
]
