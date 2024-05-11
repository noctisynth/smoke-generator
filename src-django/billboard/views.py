from django.http import JsonResponse, HttpRequest

# Create your views here.
from .models import Announcement


def latest(request: HttpRequest):
    last = Announcement.objects.last()
    if last:
        return JsonResponse(
            {
                "status": 200,
                "data": {
                    "id": last.id,  # type: ignore
                    "title": last.title,
                    "intro": last.intro,
                    "content": last.content,
                    "date": last.date,
                    "author": last.author,
                },
            }
        )
    else:
        return JsonResponse({"status": 404, "message": "暂无"})


def all(request: HttpRequest):
    a = Announcement.objects.all().reverse()
    # reverse 获取最新
    d = []
    for i in a:
        d.append(
            {
                "id": i.id,  # type: ignore
                "title": i.title,
                "intro": i.intro,
                "content": i.content,
                "date": i.date,
                "author": i.author,
            }
        )

    return JsonResponse({"status": 200, "data": d})


def get(request: HttpRequest, aid):
    a = Announcement.objects.filter(id=aid)
    if len(a) > 0:
        return JsonResponse(
            {
                "status": 200,
                "data": {
                    "id": a[0].id,  # type: ignore
                    "title": a[0].title,
                    "intro": a[0].intro,
                    "content": a[0].content,
                    "date": a[0].date,
                    "author": a[0].author,
                },
            }
        )
    else:
        return JsonResponse({"status": 404, "message": "公告不存在"})
