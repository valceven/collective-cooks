from django.db import models
from accounts.models import User
# Create your models here.

class Review(models.Model):
    poster_id = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(blank=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by : {self.poster_id} on {self.created_date}"
