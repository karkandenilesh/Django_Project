from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)
    Address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField()
    is_admin = models.BooleanField()

    def __str__(self):
        return str(self.user)

class Organization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.PositiveIntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=100)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    linkedin_url = models.URLField(max_length=200)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()

    def __str__(self):
        return self.name
