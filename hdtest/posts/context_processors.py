from taggit.models import Tag


def tags_cloud(request):
    return {
        'tags': Tag.objects.all()
    }