from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .serial import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

