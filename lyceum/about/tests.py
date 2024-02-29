import django.test
import django.urls

__all__ = ["StaticURLTests"]


class StaticURLTests(django.test.TestCase):
    def test_description_endpoint_code(self):
        response = self.client.get(django.urls.reverse("about:description"))
        self.assertEqual(response.status_code, 200)
