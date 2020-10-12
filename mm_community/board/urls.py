from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write),

]
# 어드민 하위에 있는 건 다 여기로 연결하겠다. 주소 뒤에 admin을 붙이면 장고의 관리자도구를 사용할 수 있다
