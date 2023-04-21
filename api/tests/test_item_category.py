from rest_framework.test import APITestCase

from api.models import ItemCategory


class ItemCategoryListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_categories = 15
        for category_id in range(number_of_categories):
            ItemCategory.objects.create(name=f"category_{category_id}", subcategory=f"subcategory_{category_id}")
        

    def test_url_exists(self):
        response = self.client.get("/api/item-category/")
        self.assertEqual(response.status_code, 200)

    def test_get_request_correctly_return_count(self):
        response = self.client.get("/api/item-category/")
        self.assertEqual(len(response.data['results']), 15)
