from django.db import models

class TaskModel(models.Model):
    text = models.TextField('Task')
    active = models.BooleanField('Active', default=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.text[:50]
