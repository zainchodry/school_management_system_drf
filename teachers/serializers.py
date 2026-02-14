from rest_framework import serializers
from .models import Teacher, Subject, TeacherSubject

class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Teacher
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = "__all__"
