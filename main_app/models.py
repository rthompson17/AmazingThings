from django.db import models
from django.urls import reverse

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    age = models.IntegerField()
    
    def __str__(self):
      return f"The thing names {self.name} has id of {self.id}"

      # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'thing_id': self.id})