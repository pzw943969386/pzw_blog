from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message',verbose_name='留言用户')
    content = models.TextField(max_length=256,verbose_name='留言内容')
    publish = models.DateTimeField(verbose_name='留言时间')

    def __str__(self):
        ly = '<Message:[user={user},content={content}, publish={publish}]>'
        return ly.format(user=self.user,content=self.content, publish=self.publish)

    class Meta:
        ordering = ('-publish',)
        verbose_name = verbose_name_plural = '留言'
