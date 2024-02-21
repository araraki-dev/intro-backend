from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f'ID: {self.id} {self.title}'