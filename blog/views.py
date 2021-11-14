from django.shortcuts import render

def home(request):
    posts = [
        {
            "author": "Edward Prosper",
            "content": "First Blog Post",
            "date_posted": "November 13, 2021",
            "title": "Blog Post 1"
        },
        {
            "author": "Deborah Iluonaze",
            "content": "Second Blog Post",
            "date_posted": "June 13, 2021",
            "title": "Blog Post 2"
        },
    ]

    context = {
        "posts": posts,
    }

    return render(request, "blog/home_1.html", context)

def about(request):
    return render(request, "blog/about.html")
