from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class NewsAndBlog(models.Model):
    TYPE = (('blog','Blog'),('news','News'))
    type = models.CharField(max_length=10,choices=TYPE)
    image= models.FileField(upload_to='blog_image')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,default='Admin')
    description = RichTextUploadingField()
    tag = models.ManyToManyField('Tag',related_name='news_and_blog')
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)


    def __str__(self):
        return self.title
  
    class Meta:
        ordering = ['-timestamp']

class Tag(models.Model):
    name = models.CharField(max_length=255,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    
    def __str__(self):
        return self.name
  
    class Meta:
        ordering = ['-timestamp']