from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class TodoItemListTests(APITestCase):
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

    def test_list_all_todo_items(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_with_url_parameter_json(self):
        param = {'format': 'json'}

        response = self.client.get(self.url, param)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_with_url_suffixe_dot_json(self):
        url_plus_json = self.url[:-1] + '.json'

        response = self.client.get(url_plus_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_response_payload(self):
        queryset = TodoItem.objects.all()
        serializer = TodoItemSerializer(instance=queryset, many=True)
        response = self.client.get(self.url)
        self.assertEqual(response.data, serializer.data)

    def test_response_header_content_type_is_application_json(self):
        response = self.client.get(self.url)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_response_header_allow_get(self):
        response = self.client.get(self.url)
        self.assertTrue('GET' in response.headers['allow'])


class TodoItemRetrieveTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
        }
        TodoItem.objects.create(**cls.data)

    def test_retrieve_a_todo_item(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_a_todo_item_with_url_parameter_json(self):
        param = {'format': 'json'}

        response = self.client.get(self.url, param)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_a_todo_item_with_url_suffixe_dot_json(self):
        url_plus_json = self.url[:-1] + '.json'

        response = self.client.get(url_plus_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_todo_item_with_invalid_id(self):
        url = reverse('todo-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_todo_item_by_id_response_payload(self):
        response = self.client.get(self.url)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_response_header_content_type_is_application_json(self):
        response = self.client.get(self.url)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_response_header_allow_get(self):
        response = self.client.get(self.url)
        self.assertTrue('GET' in response.headers['allow'])


class TodoItemCreateTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-list')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
        }

    def test_create_a_todo_item(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_todo_item_with_url_parameter_json(self):
        url_plus_param = self.url + '?format=json'

        response = self.client.post(url_plus_param, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_todo_item_with_url_suffixe_dot_json(self):
        url_plus_json = self.url[:-1] + '.json'

        response = self.client.post(url_plus_json, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_no_create_todo_item_with_invalid_data(self):
        invalid_data = {
            'title': 'title',
        }
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_response_payload(self):
        response = self.client.post(self.url, self.data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_response_header_content_type_is_application_json(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_response_header_allow_post(self):
        response = self.client.post(self.url, self.data)
        self.assertTrue('POST' in response.headers['allow'])


class TodoItemUpdateTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
        }
        TodoItem.objects.create(**cls.data)

    def test_update_a_todo_item(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        response = self.client.put(self.url, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_a_todo_item_with_url_parameter_json(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        url_plus_param = self.url + '?format=json'

        response = self.client.put(url_plus_param, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_a_todo_item_with_url_suffixe_dot_json(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        url_plus_json = self.url[:-1] + '.json'

        response = self.client.put(url_plus_json, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo_item_with_invalid_id(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        url = reverse('todo-detail', kwargs={'pk': 2})
        response = self.client.put(url, full_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_todo_item_with_invalid_partial_data(self):
        invalid_partial_data = {'title': 'title updated'}
        response = self.client.put(self.url, invalid_partial_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_response_payload(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        response = self.client.put(self.url, full_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_response_header_content_type_is_application_json(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        response = self.client.put(self.url, full_data)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_response_header_allow_put(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        response = self.client.put(self.url, full_data)
        self.assertTrue('PUT' in response.headers['allow'])


class TodoItemPartialUpdateTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
        }
        TodoItem.objects.create(**cls.data)

    def test_partial_update_todo_item(self):
        partial_data = {'title': 'title updated'}
        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo_item_with_url_parameter_json(self):
        partial_data = {'title': 'title updated'}
        url_plus_param = self.url + '?format=json'

        response = self.client.patch(url_plus_param, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo_item_with_url_suffixe_dot_json(self):
        partial_data = {'title': 'title updated'}
        url_plus_json = self.url[:-1] + '.json'

        response = self.client.patch(url_plus_json, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo_item_with_invalid_id(self):
        partial_data = {'title': 'title updated'}
        url = reverse('todo-detail', kwargs={'pk': 2})
        response = self.client.patch(url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_response_payload(self):
        partial_data = {'title': 'title updated'}
        response = self.client.patch(self.url, partial_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_response_header_content_type_is_application_json(self):
        partial_data = {'title': 'title updated'}
        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_response_header_allow_patch(self):
        partial_data = {'title': 'title updated'}
        response = self.client.patch(self.url, partial_data)
        self.assertTrue('PATCH' in response.headers['allow'])


class TodoItemDeleteTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
        }
        TodoItem.objects.create(**cls.data)

    def test_delete_a_todo_item(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_a_todo_item_with_url_parameter_json(self):
        url_plus_param = self.url + '?format=json'

        response = self.client.delete(url_plus_param)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_a_todo_item_with_url_suffixe_dot_json(self):
        url_plus_json = self.url[:-1] + '.json'

        response = self.client.delete(url_plus_json)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_todo_item_with_invalid_id(self):
        url = reverse('todo-detail', kwargs={'pk': 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_response_no_content_data(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.data, None)

    def test_response_header_allow_delete(self):
        response = self.client.delete(self.url)
        self.assertTrue('DELETE' in response.headers['allow'])
