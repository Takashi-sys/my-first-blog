from django import forms
from .models import Post, Comment# コメントを追加

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#追加 読者がコメントを書けるように
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)