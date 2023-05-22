from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from knox.views import LoginView as KnoxLoginView
# from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken


# Create your views here.
class UserListApiView(generics.ListCreateAPIView):
    """ api view for user """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'country'

    search_fields = (
        '^country',
        '^userid',
    )
    

class RegisterAPI(generics.GenericAPIView):
    """ register api view """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """ User sign up"""
        # encryptedpassword = make_password(request.data.get('password'))
        # data = {
        #     'email': request.data.get('email'),
        #     'password': re,
        #     'city': request.data.get('city'),
        #     'country': request.data.get('country'),
        # }
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'id': serializer.data.get('userid', None),
            },
            status=status.HTTP_201_CREATED,
        )



class LoginAPI(KnoxLoginView):
    """
    Logs in an existing user.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        # encryptedpassword = make_password(request.data.get('password'))
        # data = {
        #     'email': request.data.get('email'),
        #     'password': request.data.get('password'),
        # }
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

