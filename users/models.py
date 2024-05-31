from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class ActivationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)