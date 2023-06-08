from django.shortcuts import render
from .models import Post

# Create your views here.
def index(req):
    posts = Post.objects.all()
    return render(req, 'index.html', { 'posts': posts })

def post(req, id):
    post = Post.objects.get(id = id)
    return render(req, 'post.html', { 'post': post })