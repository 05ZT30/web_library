from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=254, verbose_name="标题")
    time = models.CharField(max_length=254, verbose_name="时间")
    content = RichTextField(verbose_name='正文内容',config_name='default',default='abc')#config_name指定ckeditor配置文件，不指定就使用default
    def __str__(self):
        return self.title
    class Meta:
        # permissions =
        verbose_name = "新闻"
        verbose_name_plural = "所有新闻"

class roll(models.Model):
    title = models.CharField(max_length=254,verbose_name="标题")
    picture = models.ImageField(upload_to='roll/',verbose_name="轮播图片")
    href = models.CharField(max_length=254, verbose_name="链接")

    def __str__(self):
        return self.title
    class Meta:
        # permissions =
        verbose_name = "轮播图"
        verbose_name_plural = "所有轮播图"
