from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=254, verbose_name="标题")
    time = models.CharField(max_length=254, verbose_name="时间")
    href = models.CharField(max_length=254, verbose_name="链接")
    html = models.TextField(verbose_name="前端代码")
    def __str__(self):
        return self.title

class roll(models.Model):
    title = models.CharField(max_length=254,verbose_name="序号")
    picture = models.ImageField(upload_to='roll/',verbose_name="轮播图片")
    href = models.CharField(max_length=254, verbose_name="链接")

    def __str__(self):
        return self.title
