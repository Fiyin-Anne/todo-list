from django.db import models
from django.contrib.auth.forms import UserCreationForm, forms

from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Person(UserCreationForm):
#     firstname = forms.CharField(max_length=30)
#     lastname = forms.CharField(max_length=30)
#     email = forms.EmailField()


