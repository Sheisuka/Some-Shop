import http
import itertools

import django.test
import django.urls
import parameterized.parameterized

__all__ = ["StaticURLTests"]


class StaticURLTests(django.test.TestCase):
    def test_catalog_item_list_code(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.parameterized.expand(
        [
            ("1", http.HTTPStatus.OK),
            ("100", http.HTTPStatus.OK),
            ("0", http.HTTPStatus.OK),
            ("-0", http.HTTPStatus.NOT_FOUND),
            ("0.1", http.HTTPStatus.NOT_FOUND),
            ("-100", http.HTTPStatus.NOT_FOUND),
            ("abc", http.HTTPStatus.NOT_FOUND),
            ("1e5", http.HTTPStatus.NOT_FOUND),
        ],
    )
    def test_catalog_item_detail_code(self, value, expected_status):
        response = self.client.get(f"/catalog/{value}/")
        self.assertEqual(response.status_code, expected_status)

    @parameterized.parameterized.expand(
        [
            (item[0], item[1][0], item[1][1])
            for item in itertools.product(
                ["converter", "re"],
                [
                    ("1", http.HTTPStatus.OK),
                    ("100", http.HTTPStatus.OK),
                    ("0", http.HTTPStatus.NOT_FOUND),
                    ("-0", http.HTTPStatus.NOT_FOUND),
                    ("-100", http.HTTPStatus.NOT_FOUND),
                    ("abc", http.HTTPStatus.NOT_FOUND),
                    ("-0.2", http.HTTPStatus.NOT_FOUND),
                    ("1e5", http.HTTPStatus.NOT_FOUND),
                ],
            )
        ],
    )
    def test_converters_code(self, prefix, value, expected_status):
        response = self.client.get(f"/catalog/{prefix}/{value}/")
        self.assertEqual(response.status_code, expected_status)
