# Generated by Django 3.1.1 on 2020-09-29 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mm_user', '0002_auto_20200926_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('resistered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mm_user.matmateuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '매트메이트 게시글',
                'verbose_name_plural': '매트메이트 게시글',
                'db_table': 'matmate_board',
            },
        ),
    ]
