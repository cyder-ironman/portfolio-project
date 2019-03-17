from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateTimeField()
    post_body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.post_body[:50]

    def post_date_pretty(self):
        return self.post_date.strftime('%b %e %Y')
