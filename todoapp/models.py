from django.db import models

from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    date_published = models.DateTimeField()
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    def __str__(self):
        return self.name