from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='分类名',max_length=100,default='暂无')

    class Meta:
        verbose_name = verbose_name_plural = '文章分类'

    def __str__(self):
        return self.name

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='作者')
    title = models.CharField(max_length=100,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created = models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    total_views = models.PositiveIntegerField(default=0,verbose_name='浏览量')
    tags = TaggableManager(blank=True,verbose_name='标签')
    img = models.ImageField(upload_to='article/%Y/%m',blank=True,verbose_name='标题图')
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE,verbose_name='分类')

    class Meta:
        ordering = ('-created',)
        verbose_name = verbose_name_plural = '文章'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    def save(self, *args, **kwargs):
        article = super(ArticlePost, self).save(*args, **kwargs)
        if self.img and not kwargs.get('update_fields'):
            image = Image.open(self.img)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.img.path)
        return article