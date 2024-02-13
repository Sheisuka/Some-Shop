from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_coffee_code_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_content_endpoint(self):
        response = Client().get("/coffee/")
        self.assertInHTML("Я чайник", response.content.decode())

