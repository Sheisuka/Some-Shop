import django.http


def item_list(request):
    return django.http.HttpResponse("Список элементов")


def item_detail(request, pk):
    return django.http.HttpResponse("Подробно элемент")


def re_view(request, value):
    return django.http.HttpResponse(value)


def converter_view(request, value):
    return django.http.HttpResponse(str(value))
