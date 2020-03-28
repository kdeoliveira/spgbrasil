from django.db import models


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

    