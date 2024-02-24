import django.http


def item_list(request):
    return django.http.HttpResponse("Список элементов")


def item_detail(request, pk):
    return django.http.HttpResponse(f"Подробно элемент {pk}")
