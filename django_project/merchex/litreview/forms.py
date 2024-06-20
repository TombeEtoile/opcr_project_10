from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):

    title = models.CharField(max_length=128)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):

    pseudo = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    year_birthday = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )