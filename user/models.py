from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=20, default='')
    address = models.CharField(default='', max_length=255)

