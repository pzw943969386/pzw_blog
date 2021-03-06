# Generated by Django 2.1.11 on 2020-05-18 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liuyan', '0002_auto_20200319_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-publish',), 'verbose_name': '留言', 'verbose_name_plural': '留言'},
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=256, verbose_name='留言内容'),
        ),
        migrations.AlterField(
            model_name='message',
            name='publish',
            field=models.DateTimeField(verbose_name='留言时间'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL, verbose_name='留言用户'),
        ),
    ]
