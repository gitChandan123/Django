
# Create your models here.
from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]

name = models.CharField(max_length=100)
image = models.ImageField(upload_to='chais/')
date_added = models.DateTimeField(default=timezone.now)
type = models.CharField(max_length=2, default='ML')

def __str__(self):
    return self.name
