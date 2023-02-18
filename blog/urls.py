from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("all",views.news_and_blog,name='news_and_blog'),
    path("detail/<slug:slug>",views.news_and_blog_details,name='news_and_blog_details'),
]
