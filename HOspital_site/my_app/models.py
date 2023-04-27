from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

CATEGOTY_CHOICES = (
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
)
class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    catagory = models.CharField(choices=CATEGOTY_CHOICES, max_length=7)
    Address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=70)
    pincode = models.IntegerField(null=True, blank=True)
    user_profile = models.ImageField(upload_to="profile_Img")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()