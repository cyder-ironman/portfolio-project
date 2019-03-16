from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateTimeField()
    post_body = models.TextField()
    image = models.ImageField(upload_to='images/')
