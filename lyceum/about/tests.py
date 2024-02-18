from django.test import TestCase


class StaticURLTests(TestCase):
    def test_description_endpoint_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_description_endpoint_content(self):
        response = self.client.get("/about/")
        self.assertEqual(response.content, "О проекте".encode())
