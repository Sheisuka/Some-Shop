class ReverseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0
    
    def __call__(self, request):
        self.count += 1

        response = self.get_response(request)

        content = response.content.decode()
        if self.count % 10 == 0:
            self.count = 0
            content = " ".join([word[::-1] for word in content.split()])
        response.content = content.encode()

        return response