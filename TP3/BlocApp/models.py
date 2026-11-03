from django.db import models


class Author(models.Model):
    bio = models.TextField(blank=True, null = True)
    def __str__(self):
        return self.bio

class BlogPost(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    created_on = models.DateTimeField(blank=True, null=True)
