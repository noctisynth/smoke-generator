import select
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse


def generate_smoke(uploaded_pic, selected_pic):
    return "url"


# Create your views here.
def func1(request: HttpRequest):
    uploaded_pic = request.POST.get("uploaded_pic")
    selected_pic = request.POST.get("selected_pic")

    res_url = generate_smoke(uploaded_pic, selected_pic)

    return JsonResponse({"status": 200, "res_url": res_url})


def model_handle(input_pic, smoke_pic, select_post):
    # 模型处理得到图片，并保存，返回url
    return "url"


def func2(request: HttpRequest):
    input_pic = request.POST.get("input_pic")
    smoke_pic = request.POST.get("smoke_pic")
    select_pos = request.POST.get("select_pos")

    res_url = model_handle(input_pic, smoke_pic, select_pos)

    return JsonResponse({"status": 200, "res_url": res_url})
