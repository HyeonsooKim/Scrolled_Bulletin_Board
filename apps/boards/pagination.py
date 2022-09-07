from rest_framework.pagination import LimitOffsetPagination

class BoardPagination(LimitOffsetPagination):
    default_limit = 20