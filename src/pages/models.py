from django.db import models

# Erase DB 
# python manage.py migrate your_app zero
# Roll back local REPO
# git reset --hard spgbrasil/dev 


class Page(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=60)
    header_title = models.CharField(max_length=60)
    header_subtitle = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)


# PAGE HOLDS MANY CONTENTS

class Content(models.Model):
    page_name = models.ForeignKey(Page, on_delete=models.CASCADE, unique=False)
    content = models.TextField()

    def __str__(self):
        return str(self.content)

    