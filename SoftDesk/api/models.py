from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import uuid


class CustomUser(AbstractUser):
    age = models.IntegerField()
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)

    def clean(self):
        if self.age < 15:
            raise ValidationError("L'utilisateur doit avoir 15 ans minimum.")

    def __str__(self):
        return self.username
