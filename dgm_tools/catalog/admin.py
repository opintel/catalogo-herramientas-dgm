from django.contrib import admin
from django.conf import settings
from .models import Post, Tag, Category


# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    """
    Clase de configuracion de la 
    vista de administracion para
    las entradas del CMS
    """
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
        'level',
        'tags',
        'public'
    ]
    search_fields = ['title', 'description']

    def save_model(self, request, obj, form, change):
        """
        Metodo que crea una entrada
        en base de datos a partir
        del formulario de creacion/edicion
        de una entrada en el admin
        """

        # Se el usuario logueado como el autor de la entrada
        if not hasattr(obj, 'author'):
            obj.author_id = request.user.id

        obj.save()

    class Media:
        js = (
            "https://cloud.tinymce.com/stable/tinymce.min.js",
            '{}{}/js/init.tinymce.js'.format(settings.STATIC_URL, settings.AWS_LOCATION)
        )
        css = {
            "all": ('{}{}/css/admin.css'.format(settings.STATIC_URL, settings.AWS_LOCATION),)
        }


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    """
    Clase de configuracion de la 
    vista de administracion para
    las categorias del CMS
    """
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
    """
    Clase de configuracion de la 
    vista de administracion para
    los tags del CMS
    """
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
