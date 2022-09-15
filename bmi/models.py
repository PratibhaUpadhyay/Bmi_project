from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Bmi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    

    def __str__(self):
        return self.user.username
