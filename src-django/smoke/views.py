from smokegenerator.settings import MEDIA_ROOT
from django.http import HttpRequest, JsonResponse
import datetime
from util import verifyToken, selectData
from .models import Record
import random
import string
import shutil


def record2json(r: Record):
    return {
        "id": r.id,  # type: ignore
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
    """
    {
        "token":"123",
        "uploaded_pic":"",
        "selected_pic":""
    }
    """

    data = selectData(request)
    token: str = data.get("token", "")
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    mask_pic: str = data.get("mask_pic", "")
    style_pic: str = data.get("style_pic", "")

    if not all([mask_pic, style_pic]):
        return JsonResponse({"status": 402, "message": "参数错误"})

    res_name = generate_smoke(mask_pic, style_pic)
    src_pic = (
        MEDIA_ROOT.joinpath("images")
        .joinpath("smoke")
        .joinpath(mask_pic.split(".")[0] + "-" + style_pic.split(".")[0] + ".jpg")
    )

    res_url = "res/" + res_name
    save_path = MEDIA_ROOT.joinpath(res_url)

    shutil.copyfile(src_pic, save_path)
    r = Record()
    r.user = ua
    r.name = res_name
    r.pic_type = "烟雾"
    r.url = "/" + res_url
    r.save()
    obj = record2json(r)

    return JsonResponse({"status": 200, "obj": obj})


def model_handle(input_pic, smoke_pic, pos1, pos2):
    # 模型处理得到图片，并保存，返回url
    name = get_name()

    return name


def joint(request: HttpRequest):
    token: str = request.POST.get("token", "")
    print(token)
    ua = verifyToken(token)

    if not ua:
        return JsonResponse({"status": 403, "message": "用户未登录"})

    input_pic = request.FILES.get("input_pic")
    smoke_id = request.POST.get("smoke_id")
    pos1 = eval(request.POST.get("pos1"))  # type: ignore
    pos2 = eval(request.POST.get("pos2"))  # type: ignore
    # 已为你 转为tuple

    if not all([input_pic, smoke_id, pos1, pos2]):
        return JsonResponse({"status": 402, "message": "参数错误"})

    input_pic_path = MEDIA_ROOT.joinpath("images").joinpath(input_pic.name)  # type: ignore
    with open(input_pic_path, "wb") as f:
        for c in input_pic.chunks():  # type: ignore
            f.write(c)

    res_name = model_handle(input_pic.name, smoke_id, pos1, pos2)  # type: ignore
    res_url = "res/" + res_name
    save_path = MEDIA_ROOT.joinpath(res_url)
    shutil.copyfile(input_pic_path, save_path)

    r = Record()
    r.user = ua
    r.name = res_name
    r.pic_type = "图片"
    r.url = "/" + res_url
    r.save()
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
    styles_dir = MEDIA_ROOT.joinpath("images").joinpath("style")
    import os

    a = ["/images/style/" + i for i in os.listdir(styles_dir)]

    return JsonResponse({"status": 200, "styles": a})


def masks(request: HttpRequest):
    masks_dir = MEDIA_ROOT.joinpath("images").joinpath("mask")
    import os

    a = ["/images/mask/" + i for i in os.listdir(masks_dir)]

    return JsonResponse({"status": 200, "masks": a})


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


def get(request: HttpRequest):
    """
    {
        "token":"123",
        "id":1
    }
    """
    data = selectData(request)

    _id = data.get("id", None)

    if not _id:
        return JsonResponse({"status": 402, "message": "参数错误"})

    a = Record.objects.filter(id=_id)
    if len(a) > 0:
        r = a[0]
        if r.visiable:
            return JsonResponse({"status": 200, "record": record2json(r)})
        else:
            token: str = data.get("token", "")
            ua = verifyToken(token)

            if r.user == ua:
                return JsonResponse({"status": 200, "record": record2json(r)})
            else:
                return JsonResponse({"status": 403, "message": "用户未登录或无权限"})
    else:
        return JsonResponse({"status": 404, "message": "记录未找到"})
