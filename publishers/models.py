from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    

    def _str_(self):
        return self.name