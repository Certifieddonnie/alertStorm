from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken


# Create your views here.
class UserListApiView(generics.ListCreateAPIView):
    """ api view for user """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'country'

    search_fields = (
        '^country',
    )
    

class RegisterAPI(generics.GenericAPIView):
    """ register api view """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """ User sign up"""
        encryptedpassword = make_password(request.data.get('password'))
        data = {
            'email': request.data.get('email'),
            'password': encryptedpassword,
            'city': request.data.get('city'),
            'country': request.data.get('country'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({ "user": serializer.data, "token": AuthToken.objects.create(user)[1]}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        """ Login API """
        data = {
            'username': request.data.get('email'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
        }
        serializer = AuthTokenSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

