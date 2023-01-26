from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from todo.models import TodoItem


class TodoItemCRUDViewSetTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.url_detail = reverse('todo-detail', kwargs={"pk": 1})
        cls.url_list = reverse('todo-list')

        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        TodoItem.objects.create(**cls.data)
        
    def test_list_all_todo_item(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_todo_item(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo_item(self):
        response = self.client.post(self.url_list, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update_put_todo_item(self):
        response = self.client.put(self.url_detail, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_patch_todo_item(self):    
        response = self.client.patch(self.url_detail, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo_item(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
    
