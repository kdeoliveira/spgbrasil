from django.db import models
from django.urls import resolve
from django.template.context_processors import request

# Erase DB 
# python manage.py migrate your_app zero
# Roll back local REPO
# git reset --hard spgbrasil/dev 

class Page(models.Model):
    name = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=60)
    header_title = models.CharField(max_length=60)
    header_subtitle = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return str(self.name)


# PAGE HOLDS MANY CONTENTS

class Content(models.Model):
    page_name = models.ForeignKey(Page, on_delete=models.CASCADE, unique=False)
    content_type = models.CharField(max_length=10, blank=True, choices=[
        ('<p>', 'Paragraph'),
        ('<li>', 'List'),
        ('<object>', 'Object'),
        ('<span>', 'Span Block'),
        ('<div>', 'Div Block'),
    ])
    content_text = models.TextField()

    # current_url = []
    # def options(self, request, *args, **kwargs):
    #     self.current_url.append(str(request.get_full_path()))

    list_of_content = []

    def save(self, *args, **kwargs):
        self.list_of_content.append(str(self.page_name))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.page_name) + " " + str(self.content_type) 


    