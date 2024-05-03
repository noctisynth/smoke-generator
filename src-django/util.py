from django.http import HttpRequest, JsonResponse
from account.models import UserAccount, UserToken
import json


def selectData(request: HttpRequest) -> dict:
    # 解析数据
    if request.method != "POST":
        return JsonResponse({"status": 405, "message": "请用POST"})
    try:
        data: dict = json.loads(request.body.decode())
    except Exception:
        return JsonResponse({"status": 400, "message": "请使用JSON"})

    return data


def verifyToken(token: str) -> UserAccount:
    # 验证身份
    if not token:
        return None

    t = UserToken.objects.filter(token=token)
    if t.count() != 0:
        return t[0].account
    else:
        return None
