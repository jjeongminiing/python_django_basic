from django.db import models


class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128,  # 최대길이
                             verbose_name='제목')  # 명명
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('mm_user.MatmateUser', on_delete=models.CASCADE,  # CASCADE: 사용자가 탈퇴하면 사용자가 쓴 모든 글을 삭제하겠다. default,null등 설정 가능
                               verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    resistered_dttm = models.DateTimeField(auto_now_add=True,  # mmuser가 저장되는 시점에 자동으로 입력됨
                                           verbose_name='등록시간')

    def __str__(self):
        return self.title
    # 문자열로 반환할때 호출하는 함수
    # 객체를 username으로 반환하여 명시하도록 함

    class Meta:
        db_table = 'matmate_board'  # 테이블명 지정
        verbose_name = '매트메이트 게시글'
        verbose_name_plural = '매트메이트 게시글'  # 장고는 기본적으로 복수형으로 보여줌. 복수형 변환할 때
