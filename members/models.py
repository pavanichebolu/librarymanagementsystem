from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Member(models.Model):
   
    membership_date = models.DateField(default=date.today)
    address = models.TextField()

    def _str_(self):
        return self.user.username
