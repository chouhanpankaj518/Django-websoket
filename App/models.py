from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    
    
class Chat(models.Model):
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE,related_name='messages')
 