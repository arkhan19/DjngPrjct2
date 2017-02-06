from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()

    img = models.ImageField(upload_to='media/')
    text = models.TextField()

    def __str__(self):
        return self.title



    def pub_date_modified(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.text[:100]