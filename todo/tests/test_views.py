from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer

    # def test_list_four_todo_items_by_page(self):    
    #     queryset = TodoItem.objects.all()
    #     serializer = TodoItemSerializer(instance=queryset, many=True)
    #     response = self.client.get(self.url)
    #     self.assertEqual(len(response.data['results']), 4 )
    
class TodoItemListTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-list')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        for i in range(10):
            TodoItem.objects.create(**cls.data)
        
    def test_list_all_todo_items_status_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_all_todo_items_response_payload(self):
        queryset = TodoItem.objects.all()
        serializer = TodoItemSerializer(instance=queryset, many=True)
        response = self.client.get(self.url)
        self.assertEqual(response.data, serializer.data) 

class TodoItemRetrieveTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={"pk": 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        TodoItem.objects.create(**cls.data)
    
    def test_get_todo_item_by_id_status_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_todo_item_by_id_response_payload(self):
        response = self.client.get(self.url)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)


class TodoItemCreateTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-list')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        
    def test_create_todo_item_status_201(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_todo_item_response_payload(self):
        response = self.client.post(self.url, self.data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

         
class TodoItemUpdateTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={"pk": 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        TodoItem.objects.create(**cls.data)
        
    def test_todo_item_update_status_200(self):
        full_data = { 
            'title': 'title updated',
            'description': 'description updated',
            'done': True
        }
        response = self.client.put(self.url, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
    def test_todo_item_update_response_payload(self):
        full_data = { 
            'title': 'title updated',
            'description': 'description updated',
            'done': True
        }
        response = self.client.put(self.url, full_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)


class TodoItemPartialUpdateTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={"pk": 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        TodoItem.objects.create(**cls.data)
        
    def test_todo_item_partial_update_status_200(self):    
        partial_data = { 
            'title': 'title updated',
        }
        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_partial_update_response_payload(self):    
        partial_data = { 
            'title': 'title updated',
        }
        response = self.client.patch(self.url, partial_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

class TodoItemDeleteTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={"pk": 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False, 
        }
        TodoItem.objects.create(**cls.data)
                
    def test_todo_item_delete_status_204(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_todo_item_delete_response_no_content_data(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.data, None)

       