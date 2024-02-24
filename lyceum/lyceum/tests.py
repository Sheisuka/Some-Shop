import django.test


class RussianReverseMiddlewareTests(django.test.TestCase):
    @django.test.override_settings(ALLOW_REVERSE=True)
    def test_reverse_russian_words_enabled(self):
        contents = dict()
        for _ in range(10):
            content = self.client.get("/coffee/").content
            contents[content] = contents.get(content, 0) + 1
        
        self.assertEqual(contents["Я чайник".encode()], 9)
        self.assertEqual(contents["Я кинйач".encode()], 1)
    
    @django.test.override_settings(ALLOW_REVERSE=False)
    def test_reverse_russian_words_disabled(self):
        contents = {
            self.client.get("/coffee/").content for _ in range(10)
        }
        self.assertIn("Я чайник".encode(), contents)
        self.assertNotIn("Я кинйач".encode(), contents)
    

