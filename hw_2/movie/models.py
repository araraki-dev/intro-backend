from django.db import models


class Movie(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=255, default='')
    producer = models.CharField(null=False, max_length=255, default='')
    duration = models.IntegerField(null=False, default=0)


    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


    def __str__(self):
        return f'id: {self.id} {self.title}'