from django.contrib import admin
from .models import Post, Tag, Category


# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    model = Post
    list_filter = (
        'title',
        'created'
    )
    list_display = (
        'title',
        'created',
        'modified',
        'public',
        'author'
    )
    fields = [
        'title',
        'description',
        'link_external_tool',
        'text',
        'category',
        'tags',
        'public'
    ]

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'author'):
            obj.author_id = request.user.id

        obj.save()

    class Media:
        js = (
            "https://cloud.tinymce.com/stable/tinymce.min.js",
            "/static/js/init.tinymce.js?13443434",
        )
        css = {
            "all": ("/static/css/admin.css?2343432",)
        }


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    model = Category
    list_filter = (
        'name',
    )
    list_display = (
        'name',
        'public'
    )
    fields = [
        'name',
        'description',
        'public'
    ]


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    model = Tag
    list_filter = (
        'tag',
    )
    list_display = (
        'tag',
        'public'
    )
    fields = [
        'tag',
        'public'
    ]
