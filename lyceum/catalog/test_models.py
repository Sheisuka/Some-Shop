import django

import catalog


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

    def test_unable_create_category_zero_weight(self):
        category_count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category = catalog.models.Category(
                name="Тестовая категория",
                slug="test-category-slug",
                weight=0,
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count,
        )

    def test_unable_create_category_heavy_weight(self):
        category_count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.category = catalog.models.Category(
                name="Тестовая категория",
                slug="test-category-slug",
                weight=32768,
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count,
        )

    def test_create_item(self):
        item_count = catalog.models.Item.objects.count()

        self.item = catalog.models.Item.objects.create(
            name="Тестовый товар",
            category=self.category,
            text="превосходно",
        )

        self.item.tags.add(self.tag)
        self.item.save()
        self.item.full_clean()

        self.assertEqual(catalog.models.Item.objects.count(), item_count + 1)

    def test_item_not_gorgeous_validator(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name="Товар тестовый",
                category=self.category,
                text="Данный товар это очень плохо",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(catalog.models.Item.objects.count(), item_count)

    def test_item_gorgeous_validator(self):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name="Товар тестовый",
            category=self.category,
            text="Данный товар это очень роскошно",
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(catalog.models.Item.objects.count(), item_count + 1)
