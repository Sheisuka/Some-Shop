import django.test

__all__ = ["StaticURLTests"]


class StaticURLTests(django.test.TestCase):
    def test_description_endpoint_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
