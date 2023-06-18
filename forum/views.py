from django.shortcuts import get_object_or_404, render, redirect
from forum.forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)  # Autentica o usuário
            login(request, user)
            return redirect('home')
    else:
        
        form = CreateUser()

    context = {
        'form': form,
    }

    return render(request, 'pages/register.html', context)

def home(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        post = Post.objects.all().order_by('-id')
        context = {
            'post':post,
            'user':user,
            'profile':profile,
        }
        return render(request, 'pages/home.html', context)
    else:
        return redirect('login_form')
    
    


def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Senha ou Usuario Incorretos")
    return render(request, 'pages/login.html')



def post(request, slug):
    
    if request.user.is_authenticated:
        user = request.user
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
        else:
            form = CommentForm()
            
        
        context = {
            'user':user,
            'post':post,
            'comments':comments,
            'form':form,
        }
    else:
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        context = {
            'post':post,
            'comments':comments,
        }
        return redirect('login_form')
    
    
    return render(request, 'pages/post.html', context)



def profile(request, slug):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, slug=slug)
        post = Post.objects.all().filter(user=profile)
        print(post)
        context = {
            'post':post,
            'profile':profile,
        }
    else:
        return redirect('login_form')
    
    return render(request, 'pages/profile.html', context)


def addPost(request):
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = profile
                post.save()

                return redirect('home')
        else:
            form = PostForm()

        context = {
                'form':form,
                'profile':profile,
            }
        return render(request, 'pages/addPost.html', context)
    else:
        return redirect('login_form')

    
    