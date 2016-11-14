from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    sex = models.CharField(blank=True, max_length=1)
    age = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
