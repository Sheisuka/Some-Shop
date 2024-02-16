class ReverseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        response = self.get_response(request)

        self.count += 1
        if self.count % 10 == 0:
            content = response.content.decode()
            self.count = 0
            content = " ".join([word[::-1] for word in content.split()])
            response.content = content.encode()

        return response
