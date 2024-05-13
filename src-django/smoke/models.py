from turtle import mode
from django.db import models
from account.models import UserAccount
import datetime


# Create your models here.


class SmokeRecord(models.Model):
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    url = models.CharField(max_length=39 * 7, verbose_name="图片地址", unique=True)
    visible = models.BooleanField(default=False, verbose_name="可见性")

    class Meta:
        verbose_name = "拼接结果"
        verbose_name_plural = "烟雾生成结果"

        def __str__(self) -> str:
            return self.name  # type: ignore


class JointRecord(models.Model):
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    url = models.CharField(max_length=39 * 7, verbose_name="图片地址", unique=True)
    visible = models.BooleanField(default=False, verbose_name="可见性")

    class Meta:
        verbose_name = "拼接结果"
        verbose_name_plural = "拼接结果"

        def __str__(self) -> str:
            return self.name  # type: ignore
