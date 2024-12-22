
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

    name = models.CharField(max_length=100,default='MASALA')
    image = models.ImageField(upload_to='chais/',default= 'chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES,default='ML')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  
     

  # Assuming `name` is a string field in your model
    def __str__(self):
        return self.name

