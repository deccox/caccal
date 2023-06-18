from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from .models import Post, Comment, Category
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=150, widget=forms.Textarea(attrs={
    'placeholder': 'Name',
}))
    desc = HTMLField()
    categoria = forms.ModelChoiceField(
        queryset=Category.objects.all(),
    )


    title.widget.attrs.update({
        "class":"postform-title",
        "id":"post-title",
    })

    categoria.widget.attrs.update({
        "class":"postform-categoria",
        "id":"post-categoria",
    })

    class Meta:
        model = Post
        fields = ['title','desc','categoria']

class CommentForm(forms.ModelForm):
    desc = HTMLField()

    class Meta:
        model = Comment
        fields = ['desc']

class CreateUser(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    username = forms.CharField(max_length=60)
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=True))
    first_name.widget.attrs.update({
        "class":"r-name",
        "id":"id-first_name",
    })
    last_name.widget.attrs.update({
        "class":"r-name",
        "id":"id-last_name",
    })

    username.widget.attrs.update({
        "class":"r-name",
        "id":"register-username",
    })
    email.widget.attrs.update({
        "class":"r-name",
        "id":"id_email",
    })
    password1.widget.attrs.update({
        "class":"r-name",
        "id":"id_password1",
    })
    password2.widget.attrs.update({
        "class":"r-name",
        "id":"id_password2",
    })

    class Meta:
        model = User
        fields = ['username', 'password1','password2','email','first_name','last_name']
        