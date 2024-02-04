from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import post
from django.template.defaultfilters import truncatewords

class LatestPostFeed(Feed):
    title='my prj'
    link=reverse_lazy('prj:post_list')
    description="this is my post description"
    
def items(self):
    return post.published.all()[:4] #objects.order_by('published')

def item_title(self,item):
    return item.title

def item_description(self,item):
    return truncatewords(item.body,30)

#{{ items.body|truncatewords:30}}

 