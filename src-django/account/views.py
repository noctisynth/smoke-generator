from django.http import JsonResponse, HttpRequest
from .models import UserAccount, UserToken
from django.contrib.auth.hashers import make_password
from util import selectData, verifyToken


def add(request: HttpRequest):
    """
    采用form表单
    """
    if request.method != "POST":
        return JsonResponse({"status": 405, "message": "请使用POST调用接口"})

    username: str = request.POST.get("username", "")
    password: str = request.POST.get("password", "")
    phone: str = request.POST.get("phone", "")
    email: str = request.POST.get("email", "")
    stauts: str = request.POST.get("status", "")
    avatar = request.FILES.get("avatar", None)

    if not all([username, password, phone, email, stauts, avatar]):
        return JsonResponse({"status": 402, "message": "参数错误"})

    if UserAccount.objects.filter(username=username).exists():
        return JsonResponse({"status": 400, "message": "用户已存在"})

    ua = UserAccount()
    ua.username = username
    ua.password = password
    ua.phone = phone
    ua.email = email
    ua.status = stauts

    ua.avatar = avatar  # type: ignore
    ua.save()

    return JsonResponse({"status": 200, "message": "用户创建成功"})


def login(request: HttpRequest):
    """
    {
        "username"  :"bash",
        "password"  :"bash123",
        "token"     :"123123"
    }

     若无则留空
    """
    data = selectData(request)

    token: str = data.get("token", "")
    ua = verifyToken(token)

    if ua:
        return JsonResponse({"status": 201, "message": "用户已登陆"})

    username: str = data.get("username", "")
    password: str = data.get("password", "")

    if not all([username, password]):
        return JsonResponse({"status": 402, "message": "参数错误"})

    q = UserAccount.objects.filter(username=username)
    if q.count() == 0:
        return JsonResponse({"status": 402, "message": "用户不存在"})

    if password != q[0].password:
        return JsonResponse({"status": 403, "message": "密码错误"})

    # create token
    token = make_password(request.session.session_key)
    ut = UserToken()
    ut.account = q[0]
    ut.token = token
    ut.save()

    return JsonResponse({"status": 200, "message": "登录成功", "token": token})


def logout(request: HttpRequest):
    data = selectData(request)
    token = data.get("token", "")
    ua = verifyToken(token)

    if ua:
        t = UserToken.objects.filter(account=ua)
        t.delete()

    return JsonResponse({"status": 200, "message": "退出成功"})


def profile(request: HttpRequest):
    """
    {
      "token": "!XqFbIUKQRG9rUCEgUOmf3nlWWi8iSwIZaiwtmIZK"
    }
    """
    data = selectData(request)
    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    res_data = {
        "username": ua.username,
        "phone": ua.phone,
        "email": ua.email,
        "status": ua.status,
        "avatar": ua.avatar.url,
    }

    return JsonResponse(res_data)


def update(request: HttpRequest):
    """
    {
        "token":"123",
        "password":"123456",
        "phone":"1233456",
        "email":"123@dfvw.qwe",
        "status":"企业",
    }
    不需要更新的直接留空
    """
    data = selectData(request)

    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    password: str = data.get("password", "")
    phone: str = data.get("phone", "")
    email: str = data.get("email", "")
    status: str = data.get("status", "")
    avatar = request.FILES.get("avatar")

    if password:
        ua.password = password
    if phone:
        ua.phone = phone
    if email:
        ua.email = email
    if status:
        ua.status = status
    if avatar:
        ua.avatar = avatar  # type: ignore # e ?

    ua.save()

    return JsonResponse({"status": 200})
