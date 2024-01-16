from django.shortcuts import render, get_object_or_404, HttpResponse
from . import models
from .models import post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView

class postListView(ListView):
    queryset = post.published.all()
    context_object_name = "post"
    peginate_by=4
    template_name = 'post/list.html'
# Create your views here.
#def post_list(request):
    #posts = post.published.all()
    #paginator=Paginator(posts,4)
    #page=request.GET.get('page')
    #try:
        #posts=paginator.page(page)
    #except PageNotAnInteger:
       # posts=paginator.page(1)
   # except EmptyPage:
  #      posts=paginator.page(paginator.num_pages)

    #return render(request, 'post/list.html', {"posts": posts , "page":page})


# 2024/01/12
def post_detail(request,year,month,day,post):
    post= get_object_or_404(post, slug=post, status="published", publish__year=year, publish__month=month,publish__day=day)
    return render(request, 'post/detail.html', {"post": post})


