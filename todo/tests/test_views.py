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

    def test_list_all_todo_items_with_format_argument_json(self):    
        format_arg = {'format': 'json'}
        response = self.client.get(self.url, format_arg)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_list_all_todo_items_with_json_format_suffixe(self):
        url_json = self.url[:-1] + '.json'    
        response = self.client.get(url_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_response_payload(self):
        queryset = TodoItem.objects.all()
        serializer = TodoItemSerializer(instance=queryset, many=True)
        response = self.client.get(self.url)
        self.assertEqual(response.data, serializer.data)
    
    def test_list_all_todo_item_response_content_type_json(self):
        response = self.client.get(self.url)
        self.assertEqual(response.headers['content-type'], 'application/json')


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
    
    def test_get_todo_item_by_id_with_format_argument_json(self):
        format_arg = {'format': 'json'}
        response = self.client.get(self.url, format_arg)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_todo_item_by_id_with_json_format_suffixe(self):
        url_json = self.url[:-1] + '.json'    
        response = self.client.get(url_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    def test_get_todo_item_by_id_response_payload(self):
        response = self.client.get(self.url)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)
    
    def test_list_todo_item_by_id_response_content_type_json(self):
        response = self.client.get(self.url)
        self.assertEqual(response.headers['content-type'], 'application/json')
    
             


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

    def test_create_todo_item_with_format_argument_json(self):
        url_format = self.url+'?format=json'
        response = self.client.post(url_format, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_todo_item_with_json_format_suffixe(self):
        url_json = self.url[:-1] + '.json'   
        response = self.client.post(url_json, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)        

    def test_create_todo_item_response_content_type_json(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.headers['content-type'], 'application/json')
    
         
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

    def test_todo_item_update_with_format_argument_json(self):
        full_data = { 
            'title': 'title updated',
            'description': 'description updated',
            'done': True
        }
        url_format = self.url+'?format=json'
        response = self.client.put(url_format, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_todo_item_update_with_json_format_suffixe(self):
        full_data = { 
            'title': 'title updated',
            'description': 'description updated',
            'done': True
        }
        url_json = self.url[:-1] + '.json'   
        response = self.client.put(url_json, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        

    def test_todo_item_update_response_content_type_json(self):
        full_data = { 
            'title': 'title updated',
            'description': 'description updated',
            'done': True
        }
        response = self.client.put(self.url, full_data)
        self.assertEqual(response.headers['content-type'], 'application/json')
    
         

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
            'title': 'title updated'
        }
        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_item_partial_update_response_payload(self):    
        partial_data = { 
            'title': 'title updated'
        }
        response = self.client.patch(self.url, partial_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_todo_item_partial_update_with_format_argument_json(self):
        partial_data = { 
            'title': 'title updated'
        }
        url_format = self.url+'?format=json'
        response = self.client.patch(url_format, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_todo_item_partial_update_with_json_format_suffixe(self):
        partial_data = { 
            'title': 'title updated'
        }
        url_json = self.url[:-1] + '.json'   
        response = self.client.patch(url_json, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    def test_todo_item_partial_update_response_content_type_json(self):
        partial_data = { 
            'title': 'title updated'
        }
        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.headers['content-type'], 'application/json')
                 
    

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

    def test_todo_item_delete_with_format_argument_json(self):
        url_format = self.url+'?format=json'
        response = self.client.delete(url_format,)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_todo_item_delete_with_json_format_suffixe(self):
        url_json = self.url[:-1] + '.json'   
        response = self.client.delete(url_json)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)     
    
       