from turtle import mode
from django.db import models
from account.models import UserAccount
import datetime


# Create your models here.
class Record(models.Model):
    STATUS_CHOICES = (
        ("烟雾", "烟雾"),
        ("图片", "图片"),
    )
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    pic_type = status = models.CharField(
        max_length=39, choices=STATUS_CHOICES, default="图片", verbose_name="类型"
    )
    date = models.DateField(verbose_name="日期", default=datetime.date.today)

    url = models.CharField(max_length=39 * 7, verbose_name="图片地址")
    visiable = models.BooleanField(default=False, verbose_name="可见性")

    class Meta:
        verbose_name = "生成结果"
        verbose_name_plural = "生成结果"

        def __str__(self) -> str:
            return self.name  # type: ignore
