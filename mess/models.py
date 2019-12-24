from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=255, null=False, blank=False, default=None)
    date = models.DateTimeField(auto_now=True)
