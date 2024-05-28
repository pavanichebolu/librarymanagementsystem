from django.db import models

# Create your models here.
from datetime import date
from books.models import Book
from members.models import Member

# Create your models here.
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(default=date.today)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()

    def _str_(self):
        return f"{self.book.title} loaned to {self.member.user.username}"

    def is_overdue(self):
        if self.return_date is None and date.today() > self.due_date:
            return True
        return False