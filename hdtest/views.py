from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render
from hdtest.posts.models import Post


def index_view(request):
    try:
        page = int(request.GET.get('page', 1))
        tag = request.GET.get('tag')
        posts = Post.objects.all().prefetch_related('author', 'comments')
        if tag:
            posts = posts.filter(tags__name=tag)

        paginator = Paginator(posts, 10)
        pagination = paginator.page(page)
    except (EmptyPage, ValueError):
        raise Http404

    return render(request, 'index.html', {'pagination': pagination})