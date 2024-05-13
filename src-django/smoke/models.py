from django.db import models
from account.models import UserAccount
import datetime
from django.utils.html import format_html

# Create your models here.


class SmokeRecord(models.Model):
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    url = models.CharField(max_length=39 * 7, verbose_name="图片地址")
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

    def save(self):
        on_update()
        super().save()

    username.short_description = "用户名"
    image.short_description = "图片"

    class Meta:
        verbose_name = "烟雾生成结果"
        verbose_name_plural = "烟雾生成结果"

        def __str__(self) -> str:
            return self.name  # type: ignore


class JointRecord(models.Model):
    name = models.CharField(max_length=39 * 3, verbose_name="名称")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="用户")
    date = models.DateField(verbose_name="日期", default=datetime.date.today)
    url = models.CharField(max_length=39 * 7, verbose_name="图片地址")
    visible = models.BooleanField(default=False, verbose_name="可见性")

    def save(self):
        on_update()
        super().save()

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

    username.short_description = "用户名"
    image.short_description = "图片"

    class Meta:
        verbose_name = "拼接结果"
        verbose_name_plural = "拼接结果"

        def __str__(self) -> str:
            return self.name  # type: ignore


def on_update():
    from public.models import PublicJoint, PublicSmoke

    public_smokes = SmokeRecord.objects.filter(visible=True)
    private_smokes = SmokeRecord.objects.filter(visible=False)

    for ps in private_smokes:
        for i in PublicSmoke.objects.filter(record=ps):
            i.delete()

    for ps in public_smokes:
        a = PublicSmoke.objects.filter(record=ps)
        if len(a) == 0:
            _p = PublicSmoke()
            _p.record = ps
            _p.save()

    public_joints = JointRecord.objects.filter(visible=True)
    private_joints = JointRecord.objects.filter(visible=False)

    for ps in private_joints:
        for i in PublicJoint.objects.filter(record=ps):
            i.delete()

    for ps in public_joints:
        a = PublicJoint.objects.filter(record=ps)
        if len(a) == 0:
            _p = PublicJoint()
            _p.record = ps
            _p.save()
