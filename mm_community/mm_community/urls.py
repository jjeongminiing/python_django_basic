from django.contrib import admin
from django.urls import path, include
from mm_user.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mmuser/', include('mm_user.urls')),
    path('board/', include('board.urls')),
    path('', home),
]
# 어드민 하위에 있는 건 다 여기로 연결하겠다. 주소 뒤에 admin을 붙이면 장고의 관리자도구를 사용할 수 있다
