from django.db import models
from teachers.models import Subject, Teacher

class SchoolClass(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Section(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    class Meta:
        unique_together = ("school_class","name")


class TimeTable(models.Model):
    DAYS = (
        ("MON","Monday"),
        ("TUE","Tuesday"),
        ("WED","Wednesday"),
        ("THU","Thursday"),
        ("FRI","Friday"),
    )

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS)
    period = models.PositiveIntegerField()

    class Meta:
        unique_together = ("school_class","section","day","period")
