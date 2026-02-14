from django.urls import path
from .views import *

urlpatterns = [
    path("classes/", ClassListCreateView.as_view()),
    path("sections/", SectionListCreateView.as_view()),
    path("timetable/", TimeTableListCreateView.as_view()),
]
