from django.urls import path
from . import views
from .models import post,comment
from .views import post_list,post_detail,post_share
from prj.feeds import LatestPostFeed




app_name='prj'

urlpatterns = [
    #path("",views.PostListView.as.view(),name="post_list"),
    path("",views.post_list,name="post_list"),
    path("tag/<slug:tag_slug>/",views.post_list,name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:Post>/",views.post_detail,name="post_detail"),
    path("<int:post_id>/share/",views.post_share,name="post_share"),
    path('feed/',LatestPostFeed(),name="post_feed"),
]    
