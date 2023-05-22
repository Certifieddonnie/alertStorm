from rest_framework import serializers
from .models import User
from django.shortcuts import get_object_or_404
from email_validator import validate_email
from django.core import exceptions
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["userid","email", "password", "date_joined", "city", "country"]

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["userid","email", "password", "date_joined", "city", "country"]
        extra_kwargs = {'password': {'write_only': True}, 'userid': {'read_only': True}, 'date_joined': {'read_only': True}}
    
    def create(self, validated_data):
        print(f"validated data ==>  {validated_data}")
        user = User.objects.create_user(**validated_data)

        return user

# class AuthCustomTokenSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if email and password:
#             # Check if user sent email
#             if validate_email(email):
#                 user_request = get_object_or_404(
#                     User,
#                     email=email,
#                 )

#                 email = user_request.email

#             user = authenticate(username=email, password=password)

#             if user:
#                 if not user.is_active:
#                     msg = 'User account is disabled.'
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg = 'Unable to log in with provided credentials.'
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = 'Must include "email" and "password"'
#             raise exceptions.ValidationError(msg)

#         attrs['user'] = user
#         return attrs

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

        return {
            'token': user.userid,
        }
