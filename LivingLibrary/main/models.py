from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=254, verbose_name="标题")
    time = models.DateTimeField('添加日期', default=timezone.now)
    content = RichTextUploadingField(verbose_name='内容',config_name='default',default='abc')#config_name指定ckeditor配置文件，不指定就使用default
    def __str__(self):
        return self.title
    class Meta:
        db_table = ''
        managed = True
        verbose_name = '新闻'
        verbose_name_plural = '新闻管理'


class roll(models.Model):
    title = models.CharField(max_length=254,verbose_name="标题")
    picture = models.ImageField(upload_to='roll/',verbose_name="图片")
    add_date = models.DateTimeField(auto_now_add=True,verbose_name="添加时间",null=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = ''
        managed = True
        verbose_name = '图片'
        verbose_name_plural = '轮播图管理'
