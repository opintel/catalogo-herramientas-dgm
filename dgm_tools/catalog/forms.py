from django import forms
from .models import Post, Category, Tag


class PostForm(forms.ModelForm):
    model = Post

    def clean_title(self):
        title = self.cleaned_data['title']
        count_posts = Post.objects.filter(title__unaccent__icontains=title).count()

        if count_posts > 0:
            raise forms.ValidationError("Ya existe una entrada con este titulo")

        return title


class CategoryForm(forms.ModelForm):
    model = Category

    def clean_name(self):
        name = self.cleaned_data['name']
        count_category = Category.objects.filter(name__unaccent__icontains=name).count()

        if count_category > 0:
            raise forms.ValidationError("Ya existe una categoría con este nombre")

        return name.lower()


class TagForm(forms.ModelForm):
    model = Tag

    def clean_tag(self):
        tag = self.cleaned_data['tag']
        count_tag = Tag.objects.filter(tag__unaccent__icontains=tag).count()

        if count_tag > 0:
            raise forms.ValidationError("Ya existe un tag con este nombre")

        return tag.lower()
