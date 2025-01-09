from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator

from .models import User, Post, Follower
import json


def index(request):
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {"page_obj": page_obj})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def new_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(user=request.user, content=content)
    return HttpResponseRedirect(reverse("index"))

def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by("-timestamp")
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    followers_count = Follower.objects.filter(user=profile_user).count()
    following_count = Follower.objects.filter(follower=profile_user).count()

    if request.user.is_authenticated:
        is_following = Follower.objects.filter(user=profile_user, follower=request.user).exists()
    else:
        is_following = False

    return render(request, "network/profile.html", {
        "profile_user": profile_user,
        "page_obj": page_obj,
        "is_following": is_following,
        "followers_count": followers_count,
        "following_count": following_count
    })

@login_required
def follow_user(request, username):
    profile_user = get_object_or_404(User, username=username)
    if request.user != profile_user:
        if Follower.objects.filter(user=profile_user, follower=request.user).exists():
            # Unfollow if already following
            Follower.objects.filter(user=profile_user, follower=request.user).delete()
        else:
            # Follow if not already following
            Follower.objects.create(user=profile_user, follower=request.user)
    return HttpResponseRedirect(reverse("profile", args=[username]))

@login_required
def like_post(request, post_id):
    if request.method == "PUT":
        post = Post.objects.get(id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return JsonResponse({"likes": post.like_count(), "liked": liked}, status=200)

@login_required
def edit_post(request, post_id):
     if request.method == "PUT":
        data = json.loads(request.body)
        content = data.get("content", "")
        try:
            post = Post.objects.get(id=post_id, user=request.user)
            post.content = content
            post.save()
            return JsonResponse({"success": True}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found or unauthorized"}, status=404)


@login_required
def following_view(request):
    following_users = Follower.objects.filter(follower=request.user).values_list('user', flat=True)
    
    posts = Post.objects.filter(user__in=following_users).order_by("-timestamp")

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", {
        "page_obj": page_obj
    })