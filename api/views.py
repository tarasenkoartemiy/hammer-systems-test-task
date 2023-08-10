from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from .serializers import PhoneSerializer, ActivateSerializer, UserSerializer
import random
import string

User = get_user_model()


class LoginAPIVIew(GenericAPIView):
    serializer_class = PhoneSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get("phone_number")

        auth_code = ''.join(random.choices(string.digits, k=4))
        own_invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        defaults = {

            'auth_code': auth_code,
            'own_invite_code': own_invite_code,
        }
        user, created = User.objects.update_or_create(
            phone_number=phone_number, defaults=defaults)

        return Response({"auth_code": auth_code}, status=HTTP_200_OK)


class ActivateAPIView(GenericAPIView):
    serializer_class = ActivateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(**serializer.data)
        except User.DoesNotExist:
            raise AuthenticationFailed('Wrong phone number or code')

        token = Token.objects.create(user=user).key

        return Response({"token": token}, status=HTTP_200_OK)


class UserAPIView(RetrieveUpdateAPIView):

    serializer_class = UserSerializer

    def get_object(self):
        phone_number = self.request.user.phone_number
        return User.objects.get(phone_number=phone_number)

