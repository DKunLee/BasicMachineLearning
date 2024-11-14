from django import forms
from .models import Post
from . import models
from django_ckeditor_5.widgets import CKEditor5Widget



category_list =[]
category_object = models.Category.objects.all()
for category in category_object:
    category_list.append(
        (f'{category.name}')
    )


class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = True

    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'category', 'thumbnail']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Title'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Short summary of the post'
                },
            ),
            'content': CKEditor5Widget(
                attrs={
                    'class': 'django_ckeditor_5'
                },
                config_name='extends',
            ),
            'category': forms.Select(
                choices=category_list,
                attrs={
                    'class':'form-control'
                },
            ),
        }
    thumbnail = forms.ImageField(required=True)

class EditPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = True

    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'category', 'thumbnail']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Title'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Short summary of the post'
                },
            ),
            'content': CKEditor5Widget(
                attrs={
                    'class': 'django_ckeditor_5'
                },
                config_name='extends',
            ),
            'category': forms.Select(
                choices=category_list,
                attrs={
                    'class':'form-control'
                },
            ),
        }
    thumbnail = forms.ImageField(required=True)