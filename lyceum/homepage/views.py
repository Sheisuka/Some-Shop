from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse("Главная")


def coffee(request):
    response = HttpResponse("Я чайник")
    response.status_code = HTTPStatus.IM_A_TEAPOT
    return response
