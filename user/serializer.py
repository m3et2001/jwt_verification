from dataclasses import field
from rest_framework import serializers
from .models import customUser

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()