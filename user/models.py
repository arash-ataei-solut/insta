from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(
        'self',
        related_name='follower',
        related_query_name='follower',
        symmetrical=False
    )
