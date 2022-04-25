from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    age = models.IntegerField()
    def __str__(self):
      return f"The thing names {self.name} has id of {self.id}"