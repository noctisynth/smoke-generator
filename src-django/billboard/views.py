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
                    "title": last.title,
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
                "title": i.title,
                "content": i.content,
                "date": i.date,
                "author": i.author,
            }
        )

    return JsonResponse({"status": 200, "data": d})
