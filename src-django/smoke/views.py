from os import name
import re
from smokegenerator.settings import MEDIA_ROOT
from django.http import HttpRequest, JsonResponse
import datetime
from util import verifyToken, selectData
from .models import Record
import random
import string


def record2json(r: Record):
    return {
        "name": r.name,
        "user": r.user.username,
        "type": r.pic_type,
        "date": r.date,
        "url": r.url,
        "visiable": r.visiable,
    }


def get_name():
    value = "".join(random.sample(string.ascii_letters + string.digits, 5))
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_datetime + value + ".jpg"


def generate_smoke(uploaded_pic, selected_pic):
    name = get_name()

    return name


# Create your views here.
def generate(request: HttpRequest):
    token: str = request.POST.get("token", "")
    uploaded_pic = request.FILES.get("uploaded_pic")
    selected_pic = request.FILES.get("selected_pic")

    if not all([token, uploaded_pic, selected_pic]):
        return JsonResponse({"status": 402, "message": "参数错误"})

    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    res_name = generate_smoke(uploaded_pic, selected_pic)

    res_url = "res/" + res_name
    r = Record()
    r.user = ua
    r.name = res_name
    r.pic_type = "烟雾"
    r.url = res_url
    r.save()
    save_path = MEDIA_ROOT.joinpath(res_url)
    obj = record2json(r)

    return JsonResponse({"status": 200, "obj": obj})


def model_handle(input_pic, smoke_pic, select_post):
    # 模型处理得到图片，并保存，返回url
    name = get_name()

    return name


def joint(request: HttpRequest):
    token: str = request.POST.get("token", "")
    input_pic = request.FILES.get("input_pic")
    smoke_pic = request.POST.get("smoke_pic")
    select_pos = request.POST.get("select_pos")
    print(token, input_pic, smoke_pic, select_pos)

    if not all([token, input_pic, smoke_pic, select_pos]):
        return JsonResponse({"status": 402, "message": "参数错误"})

    res_name = model_handle(input_pic, smoke_pic, select_pos)

    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    res_url = "res/" + res_name
    r = Record()
    r.user = ua
    r.name = res_name
    r.pic_type = "图片"
    r.url = res_url
    r.save()
    save_path = MEDIA_ROOT.joinpath(res_url)
    obj = record2json(r)
    return JsonResponse({"status": 200, "obj": obj})


def generate_history(request: HttpRequest):
    """
    {
        "token":"123"
    }
    """
    data = selectData(request)
    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})
    res = []
    for r in Record.objects.filter(user=ua, pic_type="烟雾"):
        res.append(record2json(r))

    return JsonResponse({"status": 200, "records": res})


def joint_history(request: HttpRequest):
    """
    {
        "token":"123"
    }
    """
    data = selectData(request)
    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    res = []
    for r in Record.objects.filter(user=ua, pic_type="图片"):
        res.append(record2json(r))

    return JsonResponse({"status": 200, "records": res})


def styles(request: HttpRequest):
    styles_dir = MEDIA_ROOT.joinpath("styles")
    import os

    a = ["styles/" + i for i in os.listdir(styles_dir)]

    return JsonResponse({"status": 200, "styles": a})


def update(request: HttpRequest):
    """
    {
        "token":"123",
        "url":"url",
        "type":"烟雾",
        "name":"name",
        "visiable":true,
    }
    """
    data = selectData(request)
    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    pic_type = data.get("type", 0)
    visiable = data.get("visiable", None)
    name = data.get("name", "")
    url = data.get("url", "")

    a = Record.objects.filter(user=ua, pic_type=pic_type, url=url)

    if len(a) > 0:
        if visiable:
            a[0].visiable = visiable
        if name:
            a[0].name = name
        a[0].save()
        return JsonResponse({"status": 200, "message": "已更新"})
    else:
        return JsonResponse({"status": 404, "message": "记录未找到"})


def delete(request: HttpRequest):
    """
    {
        "token":"123",
        "url":"url",
        "type":"烟雾"
    }
    """

    data = selectData(request)
    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    url = data.get("url", "")
    pic_type = data.get("type", "")

    a = Record.objects.filter(user=ua, pic_type=pic_type, url=url)

    if len(a) > 0:
        for i in a:
            i.delete()

        return JsonResponse({"status": 200, "message": "删除成功"})
    else:
        return JsonResponse({"status": 404, "message": "记录不存在"})
