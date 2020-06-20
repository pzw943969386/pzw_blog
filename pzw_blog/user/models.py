from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile',verbose_name='用户名')
    img = models.ImageField(upload_to='img/%Y/%m',blank=True,verbose_name='用户头像')
    phone = models.CharField(max_length=20, blank=True,verbose_name='用户号码')
    describe = models.TextField(max_length=500, blank=True,verbose_name='用户描述')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = verbose_name_plural = '用户信息'