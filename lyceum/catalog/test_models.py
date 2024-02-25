import django.core
import django.test
import parameterized

import catalog.models


class ModelTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="Тестовая категория",
            slug="test-category-slug",
            weight=100,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="Тестовый тег",
            slug="test-tag-slug",
        )

    def tearDown(self):
        catalog.models.Item.objects.all().delete()
        catalog.models.Tag.objects.all().delete()
        catalog.models.Category.objects.all().delete()

        super().tearDown()

    @parameterized.parameterized.expand(
        [
            (-100,),
            (-1),
            (0),
            (40000),
        ]
    )
    def test_unable_create_category_bad_weight(self, value):
        category_count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category = catalog.models.Category(
                name="Какая-то категория",
                slug="some-category-slug",
                weight=value,
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count,
        )

    @parameterized.parameterized.expand(
        [
            (1,),
            (10),
            (1000),
            (32767),
        ]
    )
    def test_create_category_good_weight(self, value):
        category_count = catalog.models.Category.objects.count()
        self.category = catalog.models.Category(
            name="Какая-то категория",
            slug="some-category-slug",
            weight=value,
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count + 1,
        )

    @parameterized.parameterized.expand(
        [
            ("роскошно!",),
            ("превосходно!",),
            ("не превосходно",),
            ("Не превосходно!",),
        ]
    )
    def test_create_item_positive(self, value):
        item_count = catalog.models.Item.objects.count()

        self.item = catalog.models.Item.objects.create(
            name="Какой-то товар",
            category=self.category,
            text=value,
        )

        self.item.save()
        self.item.full_clean()
        self.item.tags.add(self.tag)

        self.assertEqual(catalog.models.Item.objects.count(), item_count + 1)

    @parameterized.parameterized.expand(
        [("роскошный",), ("раскошный",), ("превосходный"), ("qweirtроскошно",)]
    )
    def test_create_item_negative(self, value):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name="Товар тестовый",
                category=self.category,
                text=value,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(catalog.models.Item.objects.count(), item_count)
