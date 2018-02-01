from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class Post(models.Model):
    title = models.CharField(null=False, max_length=110, verbose_name='Titulo')
    description = models.TextField(blank=True, verbose_name='Encabezado')
    slug = models.SlugField(db_index=True)
    text = models.TextField(blank=True, verbose_name='Texto')
    # Categorization
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Categoria")
    tags = models.ManyToManyField('Tag')
    # State
    public = models.BooleanField(default=False, verbose_name='Publicado')
    # Periodicity
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')

    def __str__(self):
        return 'Post: {}'.format(self.title)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        
        super(Post, self).save()

    class Meta:
        index_together = ['slug', 'public']
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'


class Category(models.Model):
    name = models.CharField(null=False, max_length=110, verbose_name='Nombre')
    slug = models.SlugField(db_index=True, editable=False)
    description = models.TextField(blank=True, verbose_name='Descripcion')
    # Periodicity
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        
        super(Category, self).save()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Tag(models.Model):
    tag = models.CharField(max_length=80)
    slug = models.SlugField(db_index=True, editable=False)
    # Periodicity
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    def __str__(self):
        return '{}'.format(self.tag)

    def save(self):
        if not self.id:
            self.slug = slugify(self.tag)
        
        super(Tag, self).save()
