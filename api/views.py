from rest_framework import routers, serializers, viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = TodoSerializer

    def get_queryset(self):

        user = self.request.user
        return Todo.objects.filter(user=user)
