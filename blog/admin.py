from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'email', 'body')
