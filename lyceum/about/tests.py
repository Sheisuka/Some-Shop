from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_description_endpoint_code(self):
        response = Client().get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_description_endpoint_content(self):
        response = Client().get("/about/")
        self.assertEqual(response.content.decode(), "<body>О проекте</body>")
