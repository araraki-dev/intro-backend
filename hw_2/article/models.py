from django.db import models

class Article(models.Model):
    title = models.CharField(null=False,max_length=255, default='')
    text = models.CharField(null=False,max_length=255, default='')
    author = models.CharField(null=False,max_length=255, default='')

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


    def __str__(self):
        return f'id: {self.id} {self.title}'