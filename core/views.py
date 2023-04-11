from core.models import RequestCounterModel
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

class RequestCounterAPIView(GenericAPIView):
    """
    An endpoint to get request count.
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = RequestCounterModel.objects.get(pk=1)
        return Response({"requests": queryset.counter}, status=status.HTTP_200_OK)

class RequestCounterResetAPIView(GenericAPIView):
    """
    An endpoint to reset request count.
    """
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        queryset = RequestCounterModel.objects.get(pk=1)
        queryset.counter = 0
        queryset.save()
        return Response({"message": "request count reset successfully"}, status=status.HTTP_202_ACCEPTED)

