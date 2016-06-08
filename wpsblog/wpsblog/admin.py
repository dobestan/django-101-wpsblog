from django.contrib import admin

from wpsblog.models import Post, Comment, NaverPost


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NaverPost)
