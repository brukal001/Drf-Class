from rest_framework import serializers
from .models import User

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=120)
#     first_name = serializers.CharField(max_length=120)
#     last_name = serializers.CharField(max_length=120)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)