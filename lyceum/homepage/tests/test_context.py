import django.test
import django.urls

import catalog.models

__all__ = ["ContextTests"]


class ContextTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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
        cls.main_published_item = catalog.models.Item.objects.create(
            is_on_main=True,
            is_published=True,
            name="Тестовый опубликованный товар",
            slug="published-item",
            text="превосходно",
        )
        cls.main_unpublished_item = catalog.models.Item.objects.create(
            is_on_main=True,
            is_published=False,
            name="Тестовый неопубликованный товар",
            slug="unpublished-item",
            text="превосходно",
        )
        cls.not_main_published_item = catalog.models.Item.objects.create(
            is_on_main=False,
            is_published=True,
            name="Тестовый опубликованный товар",
            slug="published-item",
            text="превосходно",
        )
        cls.not_main_unpublished_item = catalog.models.Item.objects.create(
            is_on_main=False,
            is_published=False,
            name="Тестовый неопубликованный товар",
            slug="unpublished-item",
            text="превосходно",
        )

        cls.published_tag.save()
        cls.unpublished_tag.save()

        cls.main_published_item.clean()
        cls.main_published_item.save()
        cls.main_unpublished_item.clean()
        cls.main_unpublished_item.save()
        cls.not_main_published_item.clean()
        cls.not_main_published_item.save()
        cls.not_main_unpublished_item.clean()
        cls.not_main_unpublished_item.save()

        cls.main_published_item.tags.add(cls.published_tag.pk)
        cls.main_published_item.tags.add(cls.unpublished_tag.pk)

        cls.not_main_published_item.tags.add(cls.published_tag.pk)
        cls.not_main_published_item.tags.add(cls.unpublished_tag.pk)

        cls.main_unpublished_item.tags.add(cls.published_tag.pk)
        cls.main_unpublished_item.tags.add(cls.unpublished_tag.pk)

        cls.not_main_unpublished_item.tags.add(cls.published_tag.pk)
        cls.not_main_unpublished_item.tags.add(cls.unpublished_tag.pk)

    def test_homepage_home_items_context(self):
        response = self.client.get(django.urls.reverse("homepage:home"))
        self.assertIn(
            "items",
            response.context,
            "В контексте нет переменной items",
        )

    def test_homepage_home_items_count(self):
        response = self.client.get(django.urls.reverse("homepage:home"))
        items = response.context["items"]
        # Только опубликованные
        self.assertEqual(
            items.count(),
            1,
            "Что-то не то с количеством товаров",
        )

    def test_catalog_item_list_tags_count(self):
        response = self.client.get(django.urls.reverse("homepage:home"))
        item = response.context["items"][0]

        # Только опубликованные
        self.assertEqual(
            item.tags.count(),
            1,
            "Что-то не то с количеством тегов",
        )
