from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from . import models

# Create your views here.
def news_and_blog(request):
    template_name='news_and_blog.html'
    news_and_blog_qs = models.NewsAndBlog.objects.all()
    paginator = Paginator(news_and_blog_qs,6)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    context={
        'obj':qs
    }
    return render(request,template_name,context)

def news_and_blog_details(request,slug):
    template_name='news_and_blog_details.html'
    qs = get_object_or_404(models.NewsAndBlog,slug=slug)
    tags = models.Tag.objects.all()
    all = models.NewsAndBlog.objects.all()[:4]
    context={
        'obj':qs,
        'tags':tags,
        'all':all
    }
    return render(request,template_name,context)
