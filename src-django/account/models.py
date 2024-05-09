from django.db import models

# Create your models here.
#   - [ ] 账号（唯一）
#   - [ ] 密码
#   - [ ] 电话
#   - [ ] 邮箱
#   - [ ] 个人/企业身份选择
#   - [ ] 头像上传


class UserAccount(models.Model):
    STATUS_CHOICES = (
        ("个人", "个人"),
        ("企业", "企业"),
    )
    username = models.CharField(unique=True, verbose_name="账号", max_length=39)
    password = models.CharField(max_length=39, verbose_name="密码")
    phone = models.CharField(max_length=39, verbose_name="电话")
    email = models.EmailField(max_length=39 * 2, verbose_name="邮箱")
    status = models.CharField(
        max_length=39, choices=STATUS_CHOICES, default="个人", verbose_name="身份"
    )
    # Image字段保存图片
    avatar = models.ImageField(
        upload_to="avatar", verbose_name="头像", default="123.jpg", null=True
    )

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

        def __str__(self) -> str:
            return self.username  # type: ignore


class UserToken(models.Model):
    token = models.CharField(
        max_length=39 * 2, verbose_name="Token", null=False, unique=True
    )
    account = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, null=False, related_name="token"
    )
