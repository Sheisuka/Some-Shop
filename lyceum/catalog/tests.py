from django.test import Client, TestCase


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
    
    def test_re_negative(self):
        response = Client().get("/catalog/re/-10/")
        self.assertEqual(response.status_code, 404)

    def test_re_letters(self):
        response = Client().get("/catalog/re/abc/")
        self.assertEqual(response.status_code, 404)   
    
    def test_re_zero(self):
        response = Client().get("/catalog/re/0/")
        self.assertEqual(response.status_code, 404)
    
    def test_re_endpoint(self):
        response = Client().get("/catalog/re/100/")
        self.assertEqual(response.status_code, 200)
