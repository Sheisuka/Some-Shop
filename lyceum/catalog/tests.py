from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail_zero_endpoint(self):
        response = Client().get("/catalog/0/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail_negative_endpoint(self):
        response = Client().get("/catalog/-10")
        self.assertEqual(response.status_code, 404)
