from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    from_frontpage = models.BooleanField(default=False)
    on_newsletter = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    