from django.urls import path
from .models import post
from . import views

app_name='prj'

urlpatterns = [
    path("",views.postListView.as_view(),name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:Post>/",views.post_detail,name="post_detail"),
    path("<int:post_id>/share/",views.post_share,name="post_share")
]    