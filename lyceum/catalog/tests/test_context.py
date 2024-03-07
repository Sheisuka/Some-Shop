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
        items = response.context["items"]

        # Только опубликованные
        self.assertEqual(items.count(), 1)

    def test_catalog_item_list_tags_count(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        item = response.context["items"][0]

        # Только опубликованные
        self.assertEqual(item.tags.count(), 1)

    def test_catalog_item_list_items_context(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        # Только опубликованные
        self.assertIn("items", response.context)

    def test_catalog_item_list_items_type(self):
        response = self.client.get(django.urls.reverse("catalog:item_list"))
        items = response.context["items"]
        for item in items:
            self.assertIsInstance(item, catalog.models.Item)
