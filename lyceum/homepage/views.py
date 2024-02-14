from django.http import HttpResponse


def home(request):
    return HttpResponse("Главная")


def coffee(request):
    response = HttpResponse("Я чайник")
    response.status_code = 418
    return response
