from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_description_endpoint(self):
        response = Client().get("/about/")
        self.assertEqual(response.status_code, 200)
