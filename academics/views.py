from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import IsAdmin

class ClassListCreateView(generics.ListCreateAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class SectionListCreateView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class TimeTableListCreateView(generics.ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
