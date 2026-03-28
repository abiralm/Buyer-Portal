from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model =User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        # Passwords are hashed automatically via create_user
        return User.objects.create_user(**validated_data)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['id', 'email', 'password', 'role']
