from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ShowAllPosts,
    PostCommentView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path("about/", views.about, name='about'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail" ),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user_posts"),
    path("posts/all/", ShowAllPosts.as_view(), name="all_posts"),
    path('post/<int:pk>/comment/', PostCommentView.as_view(), name="post_comments"),

    
]