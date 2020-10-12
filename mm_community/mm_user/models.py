from django.db import models

# Create your models here.


class MatmateUser(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32,  # 최대길이
                                verbose_name='사용자명')  # 명명
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    resistered_dttm = models.DateTimeField(auto_now_add=True,  # mmuser가 저장되는 시점에 자동으로 입력됨
                                           verbose_name='등록시간')

    def __str__(self):
        return self.username
    # 문자열로 반환할때 호출하는 함수
    # 객체를 username으로 반환하여 명시하도록 함

    class Meta:
        db_table = 'matmate_mmuser'  # 테이블명 지정
        verbose_name = '매트메이트 사용자'
        verbose_name_plural = '매트메이트 사용자'  # 장고는 기본적으로 복수형으로 보여줌. 복수형 변환할 때
