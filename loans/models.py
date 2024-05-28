from django.db import models

# Create your models here.
from datetime import date


# Create your models here.
class Loan(models.Model):
    
    loan_date = models.DateField(default=date.today)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()

    def _str_(self):
        return f"{self.book.title} loaned to {self.member.user.username}"

    