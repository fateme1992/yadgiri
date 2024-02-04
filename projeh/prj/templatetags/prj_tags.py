from django import template
from ..models import post
from django.utils.safestring import mark_safe
import markdown

register=template.Library()


@register.simple_tag
def total_posts():
    return post.published.count() 

@register.inclusion_tag('post/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts=post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
    