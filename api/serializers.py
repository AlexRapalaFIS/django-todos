from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Todo
from rest_framework.fields import CurrentUserDefault


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TodoSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "name", "description", "status", "user"]

    def create(self, validated_data):
        user = self.context['request'].user
        name = validated_data['name']
        description = validated_data['description']
        status = validated_data['status']
        return Todo.objects.create(user=user, name=name,
                                   description=description, status=status)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
