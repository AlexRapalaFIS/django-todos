from rest_framework import routers, serializers, viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("id")
    serializer_class = TodoSerializer
