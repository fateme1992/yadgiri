from django.contrib.sitemaps import Sitemap
from .models import post

class PostSitemap(Sitemap):
    changefreq='weekly'
    priority=0.5
    
 
 
def items(self):
    return post.published.all()
       
def lastmod(self,obj):
    return obj.updated