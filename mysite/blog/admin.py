from django.contrib import admin

from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "content", "date_created", "author"
    list_display_links = ("pk",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = "pk", "post", "content", "date_created", "author"
    list_display_links = ("pk",)