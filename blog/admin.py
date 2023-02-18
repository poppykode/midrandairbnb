from django.contrib import admin
from . import models
# Register your models here.
class NewsAndBlogAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['title','type']
    list_display =['title','type']
    list_filter = ('title','type')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("title",)}
    list_display_links = ('title',)
    class Meta:
        model=(models.NewsAndBlog)

admin.site.register(models.NewsAndBlog,NewsAndBlogAdmin)
admin.site.register(models.Tag)