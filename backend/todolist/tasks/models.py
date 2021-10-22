from django.db import models

# Create your models here.
class Task(models.Model):
    TASK_DONE = [
        ('done', 'DONE'),
        ('not done', 'NOT DONE')
    ]
    content = models.CharField(max_length=200)
    completion = models.BooleanField(choices=TASK_DONE)

    def __str__(self):
        return self.content

