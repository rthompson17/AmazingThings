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

TYPES = (
    ('N', 'Nature'),
    ('V', 'Visit'),
    ('T', 'Tour')
)

class Events(models.Model):
  date = models.DateField()
  type = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TYPES,
    # set the default value for meal to be 'B'
    default=TYPES[0][0]
  )

# Create a thing ForeignKey (in psql)
thing = models.ForeignKey(Thing, on_delete=models.CASCADE)

def __str__(self):
      return f"{self.get_type_display()} on {self.date}"