from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Be Expressive")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    post_choices = models.CharField(choices=POST_CHOICES, max_length=1)
    image = models.ImageField(default="newpost.jpg", upload_to="default_pics")


    def __str__(self):
        return self.title
