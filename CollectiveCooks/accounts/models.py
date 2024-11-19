from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F',('Female')
        OTHER = 'O',('Other')

    birthdate = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    details = models.TextField(max_length=254, null=True, blank=True)
    avatar = models.ImageField(null=True)

    def save(self, *args, **kwargs):

        if not self.avatar:
            if self.gender == self.Gender.MALE:
                self.avatar = 'mchef.png'
            elif self.gender == self.Gender.FEMALE:
                self.avatar = 'fchef.png'
            else:
                self.avatar = 'default_avatar'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows the {self.following.username}"