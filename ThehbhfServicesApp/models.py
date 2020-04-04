from django.db import models

# Create your models here.
class ItemCode(models.Model):
    itemcode = models.CharField(max_length = 200)
    itemname = models.CharField(max_length = 200)
    itemsize = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.itemname