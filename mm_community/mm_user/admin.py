from django.contrib import admin
from .models import MatmateUser
# Register your models here.


class MatmateUserAdmin(admin.ModelAdmin):
    # 필드들이 리스트업됨 (장고 어드민 계속 개선 가능, 커스터마이징 가능)
    list_display = ('username', 'password')


admin.site.register(MatmateUser, MatmateUserAdmin)
