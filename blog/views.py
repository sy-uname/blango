from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def index(request):
    # posts = Post.objects.filter(published_at__lte=timezone.now())
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, "blog/post-detail.html", {"post": post})