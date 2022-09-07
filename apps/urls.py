from django.urls import path, include

urlpatterns = [
    path('boards/', include('apps.boards.urls')),
]
