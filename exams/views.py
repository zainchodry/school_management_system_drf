from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import IsTeacherOrAdmin

class ExamListCreateView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]


class ResultCreateView(generics.CreateAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]


class StudentResultView(generics.ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Result.objects.filter(student__user=self.request.user)
