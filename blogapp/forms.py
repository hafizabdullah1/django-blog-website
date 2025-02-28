from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ['title', 'image', 'description', 'author']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['name', 'post', 'created', 'active']
