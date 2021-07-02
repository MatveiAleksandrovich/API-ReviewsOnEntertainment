from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


class Membership(models.Model):
    CHOICES = (
        ('ad', 'admin'),
        ('md', 'moderator'),
        ('us', 'user'),
    )
    USER = models.CharField(max_length=300)
    choices = models.CharField(max_length=300, choices=CHOICES)


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
    )
    role = CharField(
        max_length=50,
        choices=Membership.choices,
        default=Membership.USER,
    )
    bio = models.TextField(blank=True)

    @property
    def is_moderator(self):
        return self.role == Membership.MODERATOR

    @property
    def is_admin(self):
        return (
            self.role == Membership.ADMIN
            or self.is_superuser
        )
