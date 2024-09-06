from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Users
from .serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    # Ajustamos los permisos según el método HTTP
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]  # Permite que cualquier usuario cree un usuario
        return [IsAuthenticated()]  