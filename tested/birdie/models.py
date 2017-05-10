from django.db import models

class Post(models.Model):
    body = models.TextField(blank=False)

    def get_excerpt(self, str_cnt):
        return self.body[:str_cnt]

# Create your models here.
