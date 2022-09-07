import bcrypt
import requests
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import BulletinBoard
from .serializers import BulletinBoardSerializer
from .pagination import BoardPagination
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError

# 게시판의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능한 Viewset 사용
class BoardViewSet(viewsets.ModelViewSet):
    # 게시물 생성일 정렬
    queryset = BulletinBoard.objects.all().order_by('-created_at')
    serializer_class = BulletinBoardSerializer
    pagination_class = BoardPagination

    def destroy(self, request, *args, **kwargs):
        """ 비밀번호 확인 후 삭제 진행"""
        article = get_object_or_404(BulletinBoard, id=kwargs['pk'])
        input_password = request.data['password'].encode('utf-8')
        password = article.password.encode('utf-8')

        if not bcrypt.checkpw(input_password, password):
            raise PermissionDenied('비밀번호가 일치하지 않습니다.')
            # return Response(status=status.HTTP_304_NOT_MODIFIED)
        else:
            self.perform_destroy(article)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        """현재 IP 기준 날씨 정보 받아 시리얼라이저에 저장"""

        url = 'https://api.weatherapi.com/v1/current.json'
        api_key = settings.WEATHERAPI_KEY
        response = requests.get(url, params={'key': api_key, 'q': 'auto:ip'})
        if not response.ok:
            raise ValidationError('WEATHER API ERROR')
        
        data = response.json()
        weather_txt = data['current']['condition']['text']
        serializer.save(weather=weather_txt)