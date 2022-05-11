from django.urls import path
from . import views

app_name = "FeedApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("myfeed", views.myfeed, name="myfeed"),
    path("newpost", views.new_post, name="new_post"),
    path("comments/<int:post_id>/", views.comments, name="comments"),
    path("friendsfeed/", views.friendsfeed, name="friendsfeed"),
    path("friends/", views.friends, name="friends"),
]


# First you do!!


# Creates the link at the top of the path to click on the individual hyperlinks
