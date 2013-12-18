from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm


def read_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user if request.user.is_authenticated() else None
        comment.save()

    return render(request, 'posts/read.html', {'post': post, 'form': form})
