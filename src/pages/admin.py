from django.contrib import admin
from .models import Page, Content

# admin.site.register(Page)
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    #Add foreign key onto model's list
    def page_lang(self,obj):
        return obj.page_name.lang
    page_lang.admin_order_field = 'page_name_id'
    page_lang.short_description = 'Page Language'

    list_display = ['page_name', 'content_type','page_lang']
    list_filter = ('page_name__lang','content_type')
    # fields = [('page_name', 'content_type'), 'content_text']
    fieldsets = (
        ('Page Info:',{
            'fields': ('page_name', 'content_type')
        }),
        ('Text',{
            'fields':('content_text',)
        })
        )

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ['name', 'title','lang',]



