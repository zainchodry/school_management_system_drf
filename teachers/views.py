from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Subject, TeacherSubject
from .serializers import *
from .permissions import IsAdmin

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class TeacherSubjectAssignView(generics.ListCreateAPIView):
    queryset = TeacherSubject.objects.all()
    serializer_class = TeacherSubjectSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
