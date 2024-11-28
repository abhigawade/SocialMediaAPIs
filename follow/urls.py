from django.urls import path
from .views import FollowUnfollowView, FollowersView, FollowingView

urlpatterns = [
    path('follow-unfollow/', FollowUnfollowView.as_view(), name='follow-unfollow'),
    path('followers/', FollowersView.as_view(), name='followers'),
    path('following/', FollowingView.as_view(), name='following'),
]