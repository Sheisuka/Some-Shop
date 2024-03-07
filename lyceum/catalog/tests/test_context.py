import django.test
import django.urls

import catalog.models

__all__ = ["ContextTests"]


class ContextTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.published_category = catalog.models.Category.objects.create(
            is_published=True,
            name="Тестовая опубликованная категория",
            slug="published-category",
            weight=100,
        )
        cls.unpublished_category = catalog.models.Category.objects.create(
            is_published=False,
            name="Тестовая неопубликованная категория",
            slug="unpublished-category",
            weight=100,
        )
        cls.published_tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="Тестовый опубликованный тег",
            slug="published-slug",
        )
        cls.unpublished_tag = catalog.models.Tag.objects.create(
            is_published=False,
            name="Тестовый неопубликованный тег",
            slug="unpublished-slug",
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
            category=cls.unpublished_category,
        )

        cls.published_category.save()
        cls.unpublished_category.save()

        cls.published_tag.save()
        cls.unpublished_tag.save()

        cls.published_item.clean()
        cls.published_item.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

        cls.published_item.tags.add(cls.published_tag.pk)
        cls.published_item.tags.add(cls.unpublished_tag.pk)

        cls.unpublished_item.tags.add(cls.published_tag.pk)
        cls.unpublished_item.tags.add(cls.unpublished_tag.pk)

    def test_catalog_item_list_items_count(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        categories = response.context["categories"]

        items_count = 0
        for category in categories:
            items_count += category.items.count()

        # Только опубликованные
        self.assertEqual(
            items_count,
            1,
            "Что-то не то с количеством товаров",
        )

    def test_catalog_item_list_tags_count(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        category = response.context["categories"][0]
        item = category.items.all()[0]

        # Только опубликованные
        self.assertEqual(
            item.tags.count(),
            1,
            "Что-то не то с количеством тегов",
        )

    def test_catalog_item_list_categories_context(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        # Только опубликованные
        self.assertIn(
            "categories",
            response.context,
            "В констексте нет переменной categories",
        )

    def test_catalog_item_list_categories_count(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        categories = response.context["categories"]
        # Только опубликованные
        self.assertEqual(
            categories.count(),
            1,
            "Что-то не то с количеством категорий",
        )
