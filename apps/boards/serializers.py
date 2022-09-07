from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import BulletinBoard


class BulletinBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinBoard
        fields = '__all__'
