from django import template
from siteblog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('tags_tpl.html')
def get_tag():
    tags = Tag.objects.all()
    return {"tags": tags}
