from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    
    def __str__(self):
        return self.question

class KVPair(models.Model):
    key = models.CharField(unique=True)
    value = models.TextField(blank=True)
    
    def __str__(self):
        return self.key