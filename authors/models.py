from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.