from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializer


class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint to create a new User.
    """

    permission_classes = (AllowAny,)
    serializer_class = serializer.UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        token['user'] = user.username
        data = serializer.data
        data["tokens"] = {"access": str(token.access_token)}
        return Response(data['tokens'], status=status.HTTP_201_CREATED)

