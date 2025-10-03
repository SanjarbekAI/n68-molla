from django.contrib.auth import get_user_model
from django.db import models

from apps.pages.models import BaseModel

User = get_user_model()


class ProfileModel(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    country = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    post_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
