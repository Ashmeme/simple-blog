from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=120)  
    comment_text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)