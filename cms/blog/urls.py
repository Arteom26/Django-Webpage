from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from .models import Post

urlpatterns = [
	url(r'^about/', views.about, name='about'),
	url(r'^$', views.list_of_post, name='list_of_post'),
	url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
	url(r'^category/(?P<category_slug>[\w-]+)/$', views.list_of_post_by_category, name='list_post_by_category'),
	url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
	url(r'^december/2017/', views.december_2017, name='december_2017'),
]