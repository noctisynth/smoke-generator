from tabnanny import verbose
from django.db import models
import datetime


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=39 * 4, verbose_name="标题")

    content = models.TextField(max_length=39 * 100, verbose_name="内容")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    author = models.CharField(max_length=39, verbose_name="发布者", default="管理员")

    class Meta:
        verbose_name = "公告"
        verbose_name_plural = "公告"

        def __str__(self) -> str:
            return self.title  # type: ignore
