from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint_code(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_coffee_endpoint_code(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_endpoint_content(self):
        response = Client().get("/coffee/")
        self.assertInHTML("Я чайник", response.content.decode())

