from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, pk):
    return HttpResponse("<body>Подробно элемент</body>")


def re_view(request):
    return HttpResponse("<body>{number}</body>".format(number=request.path.split("/")[-2]))


def converter_view(request, value):
    return HttpResponse(f"<body>{value}</body>")
