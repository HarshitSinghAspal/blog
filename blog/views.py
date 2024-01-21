from django.shortcuts import render, HttpResponse
import os
from django.contrib import  messages
from blog.models import Post

from django.shortcuts import redirect
from blog.models import Post, BlogComment
from django.contrib.auth.models import User
# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all().order_by('title')
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, sno): 
    post=Post.objects.filter(sno=sno).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")       
    return redirect(f"/blog/{post.sno}")

def newPost(request):
    if request.method == "POST":
        title=request.POST.get('title')
        author=request.user
        content=request.POST.get('content')
        post=Post(title= title, author=author, content=content)
        post.save()
        messages.success(request, "Your New Blog has been created successfully")       
        return redirect("/blog")
    return render(request, "blog/newPost.html")

