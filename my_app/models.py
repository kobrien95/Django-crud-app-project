from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Truck(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def get_absolute_url(self):
        return reverse("truck-detail", kwargs={"truck_id": self.id})

    
    
    def __str__(self):
        return self.name
    
    
