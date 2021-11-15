from django.shortcuts import render
from .models import Post

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
