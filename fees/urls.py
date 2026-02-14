from django.urls import path
from .views import *

urlpatterns = [
    path("structure/", FeeStructureView.as_view()),
    path("assign/", StudentFeeView.as_view()),
    path("my/", MyFeesView.as_view()),
]
