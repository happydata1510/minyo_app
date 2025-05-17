from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
