from django.urls import include, path
from rest_framework import routers

from api import views
from api.api import LoginAPI, RegistrationAPI, UserAPI

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename="GetTodos")

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
]
