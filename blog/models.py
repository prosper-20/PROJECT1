from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


CATEGORY_CHOICES = (
    ('P', 'Politics'),
    ('E', 'Entertainment'),
    ('T', 'Trending'),
    ('M', 'Music'),
    ('S', 'Sports'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

POST_CHOICES = (
    ('H', 'HOT'),
    ('N', 'NEW'),
)


class Category(models.Model): # < here
    title = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    category = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    post_choices = models.CharField(choices=POST_CHOICES, max_length=1)
    image = models.ImageField(default="newpost.jpg", upload_to="default_pics")
    likes = models.ManyToManyField(User, related_name="blog_posts")


    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


    def get_absolute_url(self):
        return reverse("post_detail",  kwargs={"pk": self.pk})
        



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField('Enter your commment...')
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"pk":self.pk})



