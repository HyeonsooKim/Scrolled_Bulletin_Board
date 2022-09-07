from django.contrib.auth.hashers import make_password
import bcrypt
from rest_framework                  import status
from rest_framework.test             import APITestCase

from apps.boards.models import BulletinBoard

class TestBulletinBoard(APITestCase):
    '''
        공지게시판 TEST Code
    '''
    # Test시작전 필요한 임시 데이터 생성
    def setUp(self):
        self.board = BulletinBoard.objects.create(
        id      = 1,
        title   = "테스트케이스 게시물 제목 1",
        content = "테스트케이스 게시물 내용 1",
        password = bcrypt.hashpw('123123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        )
        self.board_url = "/api/boards/"

    # Test를 위해 생성했던 임시 데이터 삭제
    def tearDown(self):
        BulletinBoard.objects.all().delete()

    # 게시판 리스트 조회
    def test_board_list_success(self):
        self.response = self.client.get(self.board_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 게시판 상세페이지 조회
    def test_board_detail_success(self):
        self.response = self.client.get(f'{self.board_url}1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 게시판 글 작성
    def test_board_create_success(self):
        data = {
            "title"  : "테스트케이스 게시글 추가 제목 2",
            "content": "테스트케이스 게시글 추가 내용 2",
            "password": "123123"
        }

        self.response = self.client.post(self.board_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 게시판 글 업데이트
    def test_board_update_success(self):
        data = {
            "title": "테스트케이스 게시판 제목1 수정",
            "content": "테스트케이스 게시판 내용1 수정",
            "password": "123123"
        }

        self.response = self.client.put(f'{self.board_url}1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


    # 게시판 작성글 삭제
    def test_board_delete_success(self):
        data = {
            "password": "123123"
        }
        self.response = self.client.delete(f'{self.board_url}1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)