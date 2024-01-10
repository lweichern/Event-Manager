from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True) # get current date when the model is added, updating it won't change this values
    updated_date = models.DateTimeField(auto_now=True)
    tasksNotDone = models.PositiveIntegerField()

class Tasks(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True) # get current date when the model is added, updating it won't change this values
    updated_date = models.DateTimeField(auto_now=True)
    isDone = models.BooleanField(default=False)
    event = models.ForeignKey(Events, related_name="tasks", on_delete=models.CASCADE)