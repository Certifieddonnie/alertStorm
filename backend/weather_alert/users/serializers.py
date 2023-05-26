from rest_framework import serializers, fields
from .models import User, Notification
from django import forms
from django.shortcuts import get_object_or_404
from email_validator import validate_email
from django.core import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    notifications = serializers.SlugRelatedField(many=True, read_only=True, slug_field='notification')

    class Meta:
        model = User
        fields = '__all__'

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["userid","email", "password", "date_joined", "city", "country"]
        extra_kwargs = {'password': {'write_only': True}, 'userid': {'read_only': True}, 'date_joined': {'read_only': True}}
    
    def create(self, validated_data):
        # print(f"validated data ==>  {validated_data}")
        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.Serializer):
    """
    Authenticates an existing user.
    Email and password are required.
    Returns a JSON web token.
    """
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validates user data.
        """
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return user


class NotificationSerializer(serializers.ModelSerializer):
    """ form to choose notification """
    notification = serializers.MultipleChoiceField(choices=Notification.NOTIFY_CHOICES, required=False)

    class Meta:
        model = Notification
        fields = ['notification', ]


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "city", "country"]
        extra_kwargs = {}
    
    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        
        instance.email = validated_data['email']
        instance.city = validated_data['city']
        instance.country = validated_data['country']

        instance.save()

        return instance
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

