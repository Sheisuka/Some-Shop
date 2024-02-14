from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, pk):
    return HttpResponse("<body>Подробно элемент</body>")


def re_view(request):
    return HttpResponse(f"<body>{request.path.split('/')[-2]}</body>")


def converter_view(request, value):
    return HttpResponse(f"<body>{value}</body>")
