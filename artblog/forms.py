from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image', 'status',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please fill like the title'}),
        }


    featured_image = forms.ImageField(required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)