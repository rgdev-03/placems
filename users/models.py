from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    is_staff_Admin = models.BooleanField(default=False)

    

    # def is_place_or_superuser(self):
    #     return self.is_superuser or self.role == 'bs'