from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Author, Category


class PostForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all().values('name'), empty_label='-')
    # author = forms.ModelChoiceField(queryset=Author.objects.all().values('user__username'), empty_label='-')
    #
    class Meta:
       model = Post
       fields = ['title', 'text', 'category', 'author']


