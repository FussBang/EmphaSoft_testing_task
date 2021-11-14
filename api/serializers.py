from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User

class UserRegSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password',)

    def create(self, validation_data):
        user = User.objects.create(username=validation_data['username'])
        user.set_password(validation_data['password'])
        user.save()
        return user

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                    'is_staff', 'date_joined',)
        read_only_fields = ('date_joined', 'is_staff',)

class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                    'is_staff', 'date_joined',)
        read_only_fields = ('date_joined',)