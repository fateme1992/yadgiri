from django.shortcuts import render, get_object_or_404, HttpResponse
from . import models
from .models import post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

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

def post_share(request,post_id):
    post =get_object_or_404(post,id=post_id,status="published")
    
    if request.method =='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_date
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject=f"{cd['name']} recommend you "
            massage=f"{post.title}in {post_url} and {cd['comment']}"
            send_mail(
                subject,massage,"amoralashkar@gmail.com",
                [cd['to']]
            )
            
    else:
        form=EmailPostForm()
        return render(request,'prj/post/share.html',{"post":post,"form":form})
       
    
    


