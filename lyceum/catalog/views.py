from django.http import HttpResponse


def item_list(request):
    return HttpResponse("Список элементов")


def item_detail(request, pk):
    return HttpResponse("Подробно элемент")


def re_view(request, value):
    return HttpResponse(value)


def converter_view(request, value):
    return HttpResponse(str(value))
