from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50)
    blog=models.CharField(max_length=99999)
    is_active=models.BooleanField(default=1)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
