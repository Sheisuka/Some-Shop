from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_endpoint_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, "Главная".encode())

    def test_coffee_endpoint_code(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)

    def test_coffee_endpoint_content(self):
        response = self.client.get("/coffee/")
        self.assertEqual(response.content, "Я чайник".encode())
