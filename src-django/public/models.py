from django.db import models
from smoke.models import SmokeRecord, JointRecord
from django.utils.html import format_html

# Create your models here.


class PublicSmoke(models.Model):
    record = models.ForeignKey(SmokeRecord, models.CASCADE)

    def name(self):
        return self.record.name

    def date(self):
        return self.record.date

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
            self.record.url,
        )

    def username(self):
        return self.record.user.username

    def delete(self):
        self.record.delete()
        return super().delete()

    class Meta:
        verbose_name_plural = "公开烟雾"

        def __str__(self) -> str:
            return self.name  # type: ignore


class PublicJoint(models.Model):
    record = models.ForeignKey(JointRecord, models.CASCADE)

    def name(self):
        return self.record.name

    def date(self):
        return self.record.date

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
            self.record.url,
        )

    def username(self):
        return self.record.user.username

    def delete(self):
        self.record.delete()
        return super().delete()

    class Meta:
        verbose_name_plural = "公开图片"

        def __str__(self) -> str:
            return self.name  # type: ignore
