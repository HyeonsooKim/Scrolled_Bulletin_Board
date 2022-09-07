from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Blog 목록 보여주기
board_list = views.BoardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# board detail 보여주기 + 수정 + 삭제
board_detail = views.BoardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('board/', board_list),
    path('board/<int:pk>/', board_detail),
]