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
    PostCommentView,
    LikeView,
    PoliticsView,
    TrendingView,
    EntertainmentView,
    SportsView,
    CrimeView,
    LifeView,
    EducationView,
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
    path("post/like/<int:pk>/",LikeView, name="like_post"),
    path("post/politics/", views.PoliticsView, name="politics_view"),
    path("post/entertainment/", views.EntertainmentView, name="entertainment_view"),
    path("post/crime/", views.CrimeView, name="crime_view"),
    path("post/education/", views.EducationView, name="education_view"),
    path("post/life/", views.LifeView, name="life_view"),
    path("post/trending/", views.TrendingView, name="trending_view"),
    # path("post/music/", views.MusicView, name="music_view"),
    path("post/sports/", views.SportsView, name="sports_view"),


    
]