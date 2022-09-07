from rest_framework import viewsets
from .models import BulletinBoard
from .serializers import BulletinBoardSerializer

# 게시판의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능한 Viewset 사용
class BoardViewSet(viewsets.ModelViewSet):
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer
