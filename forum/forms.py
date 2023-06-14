from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from .models import Post, Comment, Category
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=400)
    desc = HTMLField()

    categoria = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Selecione a categoria',
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    desc = HTMLField()

    class Meta:
        model = Comment
        fields = ['desc']

class CreateUser(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1','password2','email','first_name','last_name']