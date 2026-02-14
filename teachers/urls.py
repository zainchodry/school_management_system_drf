from django.urls import path
from .views import *

urlpatterns = [
    path("teachers/", TeacherListCreateView.as_view()),
    path("teachers/<int:pk>/", TeacherDetailView.as_view()),
    path("subjects/", SubjectListCreateView.as_view()),
    path("assign/", TeacherSubjectAssignView.as_view()),
]
