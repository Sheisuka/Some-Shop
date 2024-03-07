import http
import itertools

import django.test
import django.urls
import parameterized.parameterized

import catalog.models

__all__ = ["StaticURLTests"]


class StaticURLTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.published_category = catalog.models.Category.objects.create(
            is_published=True,
            name="Тестовая опубликованная категория",
            slug="some-published-category",
            weight=100,
        )
        cls.published_tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="Тестовый опубликованный тег",
            slug="some-published-slug",
        )
        cls.published_item = catalog.models.Item.objects.create(
            is_published=True,
            name="Тестовый опубликованный товар",
            text="превосходно",
            category=cls.published_category,
        )
        cls.unpublished_item = catalog.models.Item.objects.create(
            is_published=False,
            name="Тестовый неопубликованный товар",
            text="превосходно",
            category=cls.published_category,
        )

        cls.published_category.save()

        cls.published_tag.save()

        cls.published_item.clean()
        cls.published_item.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

        cls.published_item.tags.add(cls.published_tag.pk)

    def test_catalog_item_list_code(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.parameterized.expand(
        [
            ("1", http.HTTPStatus.OK),
            ("-1", http.HTTPStatus.NOT_FOUND),
            ("-0", http.HTTPStatus.NOT_FOUND),
            ("0.1", http.HTTPStatus.NOT_FOUND),
            ("-100", http.HTTPStatus.NOT_FOUND),
            ("abc", http.HTTPStatus.NOT_FOUND),
            ("1e5", http.HTTPStatus.NOT_FOUND),
        ],
    )
    def test_catalog_item_detail_code(self, value, expected_status):
        if value == "1":
            value = self.published_item.id
        elif value == "-1":
            value = self.unpublished_item.id

        response = self.client.get(f"/catalog/{value}/")
        self.assertEqual(response.status_code, expected_status)

    @parameterized.parameterized.expand(
        [
            (item[0], item[1][0], item[1][1])
            for item in itertools.product(
                ["converter", "re"],
                [
                    ("1", http.HTTPStatus.OK),
                    ("-1", http.HTTPStatus.NOT_FOUND),
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
        if value == "1":
            value = self.published_item.id
        elif value == "-1":
            value = self.unpublished_item.id

        response = self.client.get(f"/catalog/{prefix}/{value}/")
        self.assertEqual(
            response.status_code,
            expected_status,
        )
