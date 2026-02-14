from django.db import models
from accounts.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={"role":"STUDENT"})
    roll_no = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.roll_no
