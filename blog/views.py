from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import CommentForm

class ShowAllPosts(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/show_posts.html"
    ordering = ["-date_posted"]
    paginate_by = 5

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = 'users/home-page.html'
    ordering = ["-date_posted"]
    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url ="/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_posted")
            


    

def home(request):

    context = {
        "posts": Post.objects.all(),
    }

    return render(request, "users/home-page.html", context)

def about(request):
    return render(request, "blog/about.html")


def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # This returns the results of the user's search
        posts = Post.objects.filter(title__contains=searched)
        return render(request, "blog/new_search_posts.html", {'searched': searched, 'posts': posts})
    else:
        return render(request, "blog/new_search_posts.html")


class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    success_url = "/"
    template_name = "blog/post_comment_form.html"

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


    
    
    
