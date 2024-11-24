from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    is_created = models.DateTimeField(auto_now_add=True)
    is_modified = models.DateTimeField(auto_now=True)
    publication_date = models.DateField()
    page_count = models.IntegerField()

    def __str__(self):
        return self.title
