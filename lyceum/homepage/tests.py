import http

import django.test 


class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_coffee_endpoint_code(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)

    def test_coffee_endpoint_content(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.content, "Я чайник".encode())
