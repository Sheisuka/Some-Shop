import http

import django.test
import django.urls

__all__ = ["StaticURLTests"]


class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint_code(self):
        response = self.client.get(django.urls.reverse("homepage:home"))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_coffee_endpoint_code(self):
        response = self.client.get(django.urls.reverse("homepage:coffee"))
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)

    @django.test.override_settings(ALLOW_REVERSE=False)
    def test_coffee_endpoint_content(self):
        response = self.client.get(django.urls.reverse("homepage:coffee"))
        self.assertEqual(response.content, "Я чайник".encode())
