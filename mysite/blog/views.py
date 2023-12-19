from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/create_comment.html', {'form': form})
