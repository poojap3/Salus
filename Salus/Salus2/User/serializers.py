from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.Serializer):

    class Meta:
        model = CustomUser
        fields = "__all__"
