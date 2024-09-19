from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password  # Import check_password
from django.utils.crypto import get_random_string
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=25, unique=True, default="anon_")  # Required field
    last_login = models.DateTimeField(null=True, blank=True)  # Add this line


    def save(self, *args, **kwargs):
        if self.pk is not None:
            super(User, self).save(*args, **kwargs)
        else:
            if not self.username or self.username.startswith('anon_'):
                self.username = f"anon_{get_random_string(6)}"

            self.password = make_password(self.password)
            
        super(User, self).save(*args, **kwargs)


    def check_password(self, raw_password):
        """Check if the given raw_password matches the user's hashed password."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} ({self.email}) ({self.username})"
