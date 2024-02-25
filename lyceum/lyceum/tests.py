import django.test


class RussianReverseMiddlewareTests(django.test.TestCase):
    @django.test.override_settings(ALLOW_REVERSE=True)
    def test_reverse_russian_words_enabled(self):
        counts = []
        for _ in range(10):
            content = self.client.get("/coffee/").content
            counts.append(content)

        count_no_reverse = counts.count("Я чайник".encode())
        count_reverse = counts.count("Я кинйач".encode())

        self.assertEqual(count_no_reverse, 9)
        self.assertEqual(count_reverse, 1)

    @django.test.override_settings(ALLOW_REVERSE=False)
    def test_reverse_russian_words_disabled(self):
        contents = {self.client.get("/coffee/").content for _ in range(10)}
        self.assertIn("Я чайник".encode(), contents)
        self.assertNotIn("Я кинйач".encode(), contents)
