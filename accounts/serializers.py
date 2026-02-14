from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from . models import Profile
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    ROLE_CHOICES = (
        ("ADMIN","Admin"),
        ("TEACHER","Teacher"),
        ("STUDENT","Student"),
    )
    email = serializers.EmailField(required=True)
    role = serializers.ChoiceField(required=True, choices=ROLE_CHOICES)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'role', 'password', 'confirm_password']
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email Already Exists")
        
        return value
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password Is Not Same")
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')

        user = User.objects.create(**validated_data, password=password)
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("full_name","phone","address","avatar")

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = self.context['request'].user

        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password Is Incorrect")
        
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError("Old Password Is InCorrect")
        
        password_validation.validate_password(attrs['new_password'], user)

        return attrs
    
    def create(self, validated_data):
        user = self.context['request'].user
        user.check_password(self.validated_data['new_password'])
        user.save()
        return user
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(validators=[validate_password])