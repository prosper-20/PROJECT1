from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path("about/", views.about, name='about'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail" )
]