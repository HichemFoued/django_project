from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Board(models.Model):
   name=models.CharField(max_length=50,unique=True) 
   description=models.CharField(max_length=150) 

   def __str__(self):
     return self.name


class Topic(models.Model):
     subject=models.CharField(max_length=255)   
     Board=models.ForeignKey(Board, related_name='topic',on_delete=models.CASCADE) 
     created_by=models.ForeignKey(User,related_name='topics', on_delete=models.CASCADE)
     created_dt=models.DateField(auto_now_add=True) 
