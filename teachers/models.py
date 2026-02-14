from django.db import models
from accounts.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={"role":"TEACHER"})
    qualification = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    class Meta:
        unique_together = ("teacher","subject","class_name","section")
