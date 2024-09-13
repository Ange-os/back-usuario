from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Users
from rest_framework import status
from .serializers import UserSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    # Ajustamos los permisos según el método HTTP
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]  # Permite que cualquier usuario cree un usuario
        return [IsAuthenticated()]  

class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # Sobrescribimos el método get_object para devolver el usuario autenticado
    def get_object(self):
        return self.request.user

class PasswordResetResquestview(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "password reset link sent"}, status=200)
        return Response(serializer.errors, status=400)

class PasswordResetConfirmView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    