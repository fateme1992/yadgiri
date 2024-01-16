from django.contrib import admin
from django.contrib.auth.models import User
from .models import post

#admin.site.register(post)
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=('title','author','slug','status','publish')
    list_filter=('status',)
    search_fields=('title','body')
    date_hierarchy='publish'
    list_editable=('status','slug','author')
