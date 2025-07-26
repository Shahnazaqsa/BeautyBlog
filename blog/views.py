from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages
from .forms import UserForm, PostForm


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            messages.success(request, "Registration Complete")
            return redirect("blog")
    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            messages.success(request, "Login Successfull")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


@login_required(login_url="login")
def addpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post Added")
            return redirect("dashboard")
    else:
        form = PostForm()

    return render(request, "addpost.html", {"form": form})


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})


def viewpost(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "viewpost.html", {"post": post})


@login_required(login_url="login")
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"posts": posts})


@login_required(login_url="login")
def editpost(request, post_id):
    posts = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated")
            return redirect("dashboard")
    else:
        form = PostForm(instance=posts)
    return render(request, "editpost.html", {"form": form, "post": posts})


@login_required(login_url="login")
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Post deleted")
    return redirect("dashboard")


@login_required(login_url="login")
def logout(request):
    user_logout(request)
    messages.success(request, "Logout")
    return redirect("login")
