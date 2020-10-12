from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'matemate_tag'
        verbose_name = '매트메이트 태그'
        verbose_name_plural = '매트메이트 태그'
