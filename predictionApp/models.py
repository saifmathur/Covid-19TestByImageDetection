from django.db import models
from datetime import datetime

# Create your models here.
'''
class InsertFile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
'''