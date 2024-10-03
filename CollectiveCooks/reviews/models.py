from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.

class Review(models.Model):
    poster_id = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(blank=False,null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by : {self.poster_id} on {self.created_date}"
