from django.db import models
from students.models import Student
from academics.models import SchoolClass

class FeeStructure(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.school_class} - {self.amount}"


class StudentFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    due_date = models.DateField()
