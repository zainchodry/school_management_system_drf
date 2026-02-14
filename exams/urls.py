from django.urls import path
from .views import *

urlpatterns = [
    path("exams/", ExamListCreateView.as_view()),
    path("results/add/", ResultCreateView.as_view()),
    path("results/me/", StudentResultView.as_view()),
]
