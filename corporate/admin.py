from django.contrib import admin
from . import models

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['property_type','property_address']
    list_display =['property_type','property_address']
    list_filter = ('property_type','property_address')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("property_type","property_address",)}
    list_display_links = ('property_address',)
    class Meta:
        model=(models.Property)

class AgentAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['full_name','position']
    list_display =['full_name','position']
    list_filter = ('full_name','position')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("full_name",)}
    list_display_links = ('full_name',)
    class Meta:
        model=(models.Agent)

class GeneralPageAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['name','timestamp']
    list_display =['name','timestamp']
    list_filter = ('name','timestamp')
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("name",)}
  
    class Meta:
        model=(models.GeneralPage)

admin.site.register(models.Slider)
admin.site.register(models.Booking)
admin.site.register(models.GeneralPage,GeneralPageAdmin)
admin.site.register(models.Property,PropertyAdmin)
admin.site.register(models.Amenity)
admin.site.register(models.Agent,AgentAdmin)
admin.site.register(models.PropertyImage)
