from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


STATUS_CHOICES = (
    (1, _("Not relevant")),
    (2, _("Review")),
    (3, _("Maybe relevant")),
    (4, _("Relevant")),
    (5, _("Leading candidate"))
)


class Membership(models.Model):
    models.IntegerField(choices=STATUS_CHOICES, default=1)


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
