from django.db import models
from account.models import UserAccount
import datetime
from django.utils.html import format_html

# Create your models here.


class SmokeRecord(models.Model):
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    url = models.CharField(max_length=39 * 7, verbose_name="图片地址", unique=True)
    visible = models.BooleanField(default=False, verbose_name="可见性")

    def image(self):
        return format_html(
            """<img
    src="{}"
    width="100px"
    alt="图像"
    onclick="document.getElementById('modal').style.display = 'block';document.getElementById('modal-image').src=this.src;"
/>

<div
    id="modal"
    style="
        display: none;
        position: fixed;
        z-index: 9999;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
    "
    onclick="document.getElementById('modal').style.display = 'none';"
>
    <img
        id="modal-image"
        style="
            display: block;
            max-width: 90%;
            max-height: 90%;
            margin: auto;
            margin-top: 5%;
        "
    />
</div>
""",
            self.url,
        )

    def username(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "烟雾生成结果"

        def __str__(self) -> str:
            return self.name  # type: ignore


class JointRecord(models.Model):
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    url = models.CharField(max_length=39 * 7, verbose_name="图片地址", unique=True)
    visible = models.BooleanField(default=False, verbose_name="可见性")

    def image(self):
        return format_html(
            """<img
    src="{}"
    width="100px"
    alt="图像"
    onclick="document.getElementById('modal').style.display = 'block';document.getElementById('modal-image').src=this.src;"
/>

<div
    id="modal"
    style="
        display: none;
        position: fixed;
        z-index: 9999;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
    "
    onclick="document.getElementById('modal').style.display = 'none';"
>
    <img
        id="modal-image"
        style="
            display: block;
            max-width: 90%;
            max-height: 90%;
            margin: auto;
            margin-top: 5%;
        "
    />
</div>
""",
            self.url,
        )

    def username(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "拼接结果"

        def __str__(self) -> str:
            return self.name  # type: ignore
