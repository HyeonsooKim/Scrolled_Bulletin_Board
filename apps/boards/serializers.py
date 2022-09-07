import bcrypt
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError, PermissionDenied

from .models import BulletinBoard


class BulletinBoardSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    class Meta:
        model = BulletinBoard
        fields = '__all__'

    def create(self, validated_data):
        """ 비밀번호를 bcrypt 모듈을 활용하여 암호화한 후 게시물 생성"""
        password = validated_data.pop('password').encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        decoded_password = hashed_password.decode('utf-8')

        board = BulletinBoard.objects.create(password=decoded_password, **validated_data)
        return board

    def validate(self, attrs):
        """ 비밀번호 검증 : 6자리 이상, 숫자 1개 포함"""
        if len(attrs['password']) >= 6 and any(temp.isdigit() for temp in attrs['password']):
            return attrs
        else:
            raise ValidationError({'password', '비밀번호는 6자 이상이어야 하고, 숫자 1개 이상 반드시 포함되어야 합니다.'})

    def update(self, instance, validated_data):
        """ 게시물 확인 후 업데이트"""

        input_password = validated_data['password'].encode('utf-8')
        password = instance.password.encode('utf-8')

        # 비밀번호 확인
        if not bcrypt.checkpw(input_password, password):
            raise PermissionDenied('비밀번호가 일치하지 않습니다.')

        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()
        return instance