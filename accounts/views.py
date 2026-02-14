from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status
from . models import *
from . serializers import *
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = ProfileSerializer(request.user.profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Profile updated"})
    
class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail":"Password Change Successfully"}, status=status.HTTP_201_CREATED)
    
class ForgotPasswordView(APIView):
    def post(self, request):
        s = ForgotPasswordSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        user = get_object_or_404(User, email=s.data["email"])
        token = default_token_generator.make_token(user)

        send_mail("Reset Password", f"Your token: {token}", "admin@school.com", [user.email])
        return Response({"message":"Reset token sent"})


class ResetPasswordView(APIView):
    def post(self, request):
        s = ResetPasswordSerializer(data=request.data)
        s.is_valid(raise_exception=True)

        user = get_object_or_404(User)
        if not default_token_generator.check_token(user, s.data["token"]):
            return Response({"error":"Invalid token"}, status=400)

        user.set_password(s.data["new_password"])
        user.save()
        return Response({"message":"Password reset successful"})
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"detail":"Refresh Token Is Required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail":"Logout Successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"detail":"Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
