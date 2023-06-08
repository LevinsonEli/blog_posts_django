from django.shortcuts import render
from .models import Post

# Create your views here.
def index(req):
    posts = Post.objects.all()
    return render(req, 'index.html', { 'posts': posts })

def post(req, id):
    post = Post.objects.get(id = id)
    return render(req, 'post.html', { 'post': post })

def editPost(req, id):
    if req.method == "GET":
        post = Post.objects.get(id = id)
        return render(req, 'editPost.html', { 'post': post })
    elif req.method == "POST":
        post = Post.objects.get(id = id)
        post.title = req.POST["title"]
        post.body = req.POST["body"]
        post.save()
        return render(req, 'post.html', { 'post': post })

