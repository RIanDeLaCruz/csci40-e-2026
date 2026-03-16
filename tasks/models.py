from django.db import models
from django.urls import reverse

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(
        TaskGroup,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    task_image = models.ImageField(
        upload_to="images/",
        null=True
    )

    def __str__(self):
        return '{} due on {}'.format(self.name, self.due_date)

    def get_absolute_url(self):
        return reverse('tasks:task_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
