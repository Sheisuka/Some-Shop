from django.test import modify_settings, TestCase


class ReverseMiddlewareTests(TestCase):
    def __init__(self, *args, **kwargs):
        self.count = 10  # Each count-th is supposed to be reversed
        self.url = "/coffee/"
        self.default_res = "Я чайник"
        self.reversed_res = "Я кинйач"
        super().__init__(*args, **kwargs)

    @modify_settings(
        MIDDLEWARE={"append": "lyceum.middleware.ReverseMiddleware"}
    )
    def test_reversing(self):
        for i in range(1, self.count + 1):
            response = self.client.get(self.url).content.decode()
            if i % self.count:
                self.assertEqual(self.default_res, response)
            else:
                self.assertEqual(self.reversed_res, response)

    @modify_settings(
        MIDDLEWARE={"remove": "lyceum.middleware.ReverseMiddleware"}
    )
    def test_disabled(self):
        result = self.is_reversing()
        self.assertEqual(result, False)

    @modify_settings(
        MIDDLEWARE={"append": "lyceum.middleware.ReverseMiddleware"}
    )
    def test_enabled(self):
        result = self.is_reversing()
        self.assertEqual(result, True)

    def is_reversing(self):
        for i in range(self.count):
            result = self.client.get(self.url).content.decode()

        return self.reversed_res == result
