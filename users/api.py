from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, UserDetailSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserDetailSerializer
        else:
            return UserSerializer
    