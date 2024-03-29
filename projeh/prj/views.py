from django.shortcuts import render, get_object_or_404
from . import models
from .models import post ,comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm , CommentForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Count

# Create your views here. 
def post_list(request,tag_slug=None):
    posts = post.published.all()         
    tag=None
    if tag_slug:
        tag=get_object_or_404(tag,slug=tag_slug)
        posts=posts.filter(tag__in=[tag])
        
        
    paginator=Paginator(posts,4)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        Post=paginator.page(paginator.num_pages)

    return render(request, 'post/list.html', {"posts": posts , "page":page})


#class postListView(ListView):
    #queryset = post.published.all()
    #context_object_name = "posts"
    #peginate_by= 2
    #template_name = 'post/list.html'
    
      
# 2024/01/12
def post_detail(request,year,month,day,Post):
    Post= get_object_or_404(post, slug=Post,status="published",publish__year=year, publish__month=month,publish__day=day)
    comments=Post.comments.filter(active=True)
    
    
    post_tags_ids=Post.tags.values_list('id',flat=True)
    similar_posts=post.published.filter(tags__in=post_tags_ids).exclude(id=Post.id)
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')
    
    if request.method =='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.Post=Post
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:   
        comment_form=CommentForm()
        context={'Post':Post,
                 'form':comment_form,
                 'comments':comments
                 }
        return render(request, 'post/detail.html',context)

def post_share(request,post_id):
    Post =get_object_or_404(post,id=post_id,status="published")
     
    if request.method =='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid(): 
            cd =form.cleaned_data
            Post_url= request.build_absolute_uri(
                Post.get_absolute_url())
            
            subject=f"{cd['name']} recommend you "
            massage=f"{Post.title} in {Post_url} and {cd['comment']}"
            send_mail(
                subject,massage,"amoralashkar@gmail.com",
                [cd['to']]
            )
            
    else:
        form=EmailPostForm()
        return render(request,'post/share.html',{'Post':Post,'form':form})
       
    
    


