from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>Главная</body>")

def coffee(request):
    response = HttpResponse("<body>Я чайник</body>")
    response.status_code = 418
    return response
