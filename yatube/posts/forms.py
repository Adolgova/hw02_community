from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {
            'text': 'Текст поста',
            'group': 'Группа'
        }
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост'
        }
        widgets = {'text': forms.Textarea}
        fields = ('text', 'group')

