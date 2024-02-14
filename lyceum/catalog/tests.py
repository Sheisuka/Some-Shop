from django.test import Client, TestCase


class ItemListTests(TestCase):
    def test_item_list_code(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_item_list_content(self):
        response = Client().get("/catalog/")
        self.assertEqual(
            response.content, "Список элементов".encode()
        )


class ItemDetailTests(TestCase):
    def test_item_detail_zero_code(self):
        response = Client().get("/catalog/0/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail_negative_code(self):
        response = Client().get("/catalog/-10")
        self.assertEqual(response.status_code, 404)


class ReTests(TestCase):
    def test_re_negative_code(self):
        response = Client().get("/catalog/re/-10/")
        self.assertEqual(response.status_code, 404)

    def test_re_letters_code(self):
        response = Client().get("/catalog/re/abc/")
        self.assertEqual(response.status_code, 404)

    def test_re_zero_code(self):
        response = Client().get("/catalog/re/0/")
        self.assertEqual(response.status_code, 404)

    def test_re_code(self):
        response = Client().get("/catalog/re/100/")
        self.assertEqual(response.status_code, 200)

    def test_re_content(self):
        response = Client().get("/catalog/re/100/")
        self.assertEqual(response.content, "100".encode())


class ConverterTests(TestCase):
    def test_converter_code(self):
        response = Client().get("/catalog/converter/100/")
        self.assertEqual(response.status_code, 200)

    def test_converter_content(self):
        response = Client().get("/catalog/converter/50/")
        self.assertEqual(response.content.decode(), "50".encode())

    def test_converter_letters_code(self):
        response = Client().get("/catalog/converter/abc/")
        self.assertEqual(response.status_code, 404)

    def test_converter_negative_code(self):
        response = Client().get("/catalog/converter/-10/")
        self.assertEqual(response.status_code, 404)
