from django.contrib import admin
from .models import Page, Content

# admin.site.register(Page)
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'content_type')
    list_filter = ('page_name','content_type')
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
    list_display = ['name', 'title']



