from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Booking(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(default=timezone.now)
    count_people = models.PositiveIntegerField(default=1)
    special_request = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.username} - {self.date}"

class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return f"{self.username} - {self.subject}"

class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.username} - {self.telephone} - {self.address} - {self.date_of_birth}"



