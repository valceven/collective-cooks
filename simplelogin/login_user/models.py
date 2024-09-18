from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if User.objects.filter(email = self.email).exists():
            raise ValidationError

        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)
