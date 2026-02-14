from django.urls import path
from .views import *

urlpatterns = [
    path("mark/", MarkAttendanceView.as_view()),
    path("list/", AttendanceListView.as_view()),
]
