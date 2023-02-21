from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import (
    APIClient,
    APIRequestFactory,
    APITestCase,
    force_authenticate,
)

from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from todo.views import TodoItemCRUDViewSet


class TodoItemListTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-list')
        cls.user = User.objects.create_user(username='test', password='123456')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'author': cls.user,
        }
        for i in range(10):
            TodoItem.objects.create(**cls.data)

    def test_list_all_todo_items(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_with_query_param_json(self):
        query_param = {'format': 'json'}

        self.client.force_authenticate(self.user)

        response = self.client.get(self.url, query_param)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_with_url_suffix_dot_json(self):
        url_suffix_json = self.url[:-1] + '.json'
        self.client.force_authenticate(self.user)

        response = self.client.get(url_suffix_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_todo_items_response_body(self):
        queryset = TodoItem.objects.all()
        serializer = TodoItemSerializer(instance=queryset, many=True)

        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.data, serializer.data)

    def test_list_all_todo_items_response_content_type_is_json(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_list_all_todo_items_response_header_allow_get(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        self.assertTrue('GET' in response.headers['allow'])


class TodoItemRetrieveTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.user = User.objects.create_user(username='test', password='123456')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'author': cls.user,
        }
        TodoItem.objects.create(**cls.data)

    def test_retrieve_a_todo_item(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_a_todo_item_with_query_param_json(self):
        query_param = {'format': 'json'}
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url, query_param)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_a_todo_item_with_url_suffix_dot_json(self):
        url_suffix_json = self.url[:-1] + '.json'
        self.client.force_authenticate(self.user)

        response = self.client.get(url_suffix_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_a_todo_item_not_found(self):
        url = reverse('todo-detail', kwargs={'pk': 2})
        self.client.force_authenticate(self.user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_a_todo_item_response_body(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_a_todo_item_content_type_is_json(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_retrieve_a_todo_item_response_header_allow_get(self):
        self.client.force_authenticate(self.user)

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
        cls.user = User.objects.create_user(username='test', password='123456')

    def test_create_a_todo_item(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_todo_item_with_query_param_json(self):
        url_query_param = self.url + '?format=json'

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url_query_param, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_todo_item_with_url_suffix_dot_json(self):
        url_suffix_json = self.url[:-1] + '.json'

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url_suffix_json, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_create_a_todo_item_with_invalid_data(self):
        invalid_data = {
            'title': 'title',
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_a_todo_item_response_body(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, self.data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_create_a_todo_item_response_content_type_is_json(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, self.data)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_create_a_todo_item_response_header_allow_post(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, self.data)
        self.assertTrue('POST' in response.headers['allow'])

    def test_create_a_todo_item_request_content_type_is_json(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')

        force_authenticate(request, user=self.user)

        post_view = TodoItemCRUDViewSet.as_view({'post': 'create'})
        response = post_view(request)
        self.assertEqual(request.content_type, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TodoItemUpdateTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.user = User.objects.create_user(username='test', password='123456')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'author': cls.user,
        }
        TodoItem.objects.create(**cls.data)

    def test_update_a_todo_item(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        self.client.force_authenticate(self.user)

        response = self.client.put(self.url, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_a_todo_item_with_query_param_json(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        url_query_param = self.url + '?format=json'

        self.client.force_authenticate(self.user)

        response = self.client.put(url_query_param, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_a_todo_item_with_url_suffix_dot_json(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        url_suffix_json = self.url[:-1] + '.json'

        self.client.force_authenticate(self.user)

        response = self.client.put(url_suffix_json, full_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_a_todo_item_not_found(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        self.client.force_authenticate(self.user)

        url = reverse('todo-detail', kwargs={'pk': 2})
        response = self.client.put(url, full_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_not_update_a_todo_item_with_invalid_data(self):
        invalid_partial_data = {'title': 'title updated'}
        self.client.force_authenticate(self.user)

        response = self.client.put(self.url, invalid_partial_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_todo_item_response_body(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        self.client.force_authenticate(self.user)

        response = self.client.put(self.url, full_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_update_a_todo_item_response_content_type_json(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        self.client.force_authenticate(self.user)

        response = self.client.put(self.url, full_data)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_update_a_todo_item_response_header_allow_put(self):
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        self.client.force_authenticate(self.user)

        response = self.client.put(self.url, full_data)
        self.assertTrue('PUT' in response.headers['allow'])

    def test_update_a_todo_item_request_content_type_is_json(self):
        factory = APIRequestFactory()
        full_data = {
            'title': 'title updated',
            'description': 'description updated',
            'done': True,
        }
        url = reverse('todo-list')
        request = factory.put(url, full_data, format='json')
        force_authenticate(request, self.user)
        update_view = TodoItemCRUDViewSet.as_view({'put': 'update'})

        response = update_view(request, pk=1)
        self.assertEqual(request.content_type, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoItemPartialUpdateTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.user = User.objects.create_user(username='test', password='123456')

        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'author': cls.user,
        }
        TodoItem.objects.create(**cls.data)

    def test_partial_update_todo_item(self):
        partial_data = {'title': 'title updated'}
        self.client.force_authenticate(self.user)

        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo_item_with_query_param_json(self):
        partial_data = {'title': 'title updated'}
        url_query_param = self.url + '?format=json'
        self.client.force_authenticate(self.user)

        response = self.client.patch(url_query_param, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo_item_with_url_suffix_dot_json(self):
        partial_data = {'title': 'title updated'}
        url_suffix_json = self.url[:-1] + '.json'
        self.client.force_authenticate(self.user)

        response = self.client.patch(url_suffix_json, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_todo_item_not_found(self):
        partial_data = {'title': 'title updated'}
        url = reverse('todo-detail', kwargs={'pk': 2})
        self.client.force_authenticate(self.user)

        response = self.client.patch(url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_todo_item_response_body(self):
        partial_data = {'title': 'title updated'}
        self.client.force_authenticate(self.user)

        response = self.client.patch(self.url, partial_data)
        todo_item = TodoItem.objects.get(pk=1)
        serializer = TodoItemSerializer(instance=todo_item)
        self.assertEqual(response.data, serializer.data)

    def test_partial_update_todo_item_response_content_type_is_json(self):
        partial_data = {'title': 'title updated'}
        self.client.force_authenticate(self.user)

        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_partial_update_todo_item_response_header_allow_patch(self):
        partial_data = {'title': 'title updated'}
        self.client.force_authenticate(self.user)

        response = self.client.patch(self.url, partial_data)
        self.assertTrue('PATCH' in response.headers['allow'])

    def test_partial_update_todo_item_request_content_type_is_json(self):
        factory = APIRequestFactory()

        partial_data = {'title': 'title updated'}
        url = reverse('todo-list')
        request = factory.patch(url, partial_data, format='json')

        force_authenticate(request, self.user)

        partial_update_view = TodoItemCRUDViewSet.as_view(
            {'patch': 'partial_update'}
        )

        response = partial_update_view(request, pk=1)
        self.assertEqual(request.content_type, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoItemDeleteTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('todo-detail', kwargs={'pk': 1})
        cls.user = User.objects.create_user(username='test', password='123456')
        cls.data = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'author': cls.user,
        }
        TodoItem.objects.create(**cls.data)

    def test_delete_a_todo_item(self):
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_a_todo_item_with_query_param_json(self):
        url_query_param = self.url + '?format=json'
        self.client.force_authenticate(self.user)

        response = self.client.delete(url_query_param)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_a_todo_item_with_url_suffix_dot_json(self):
        url_suffix_json = self.url[:-1] + '.json'
        self.client.force_authenticate(self.user)

        response = self.client.delete(url_suffix_json)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_todo_item_not_found(self):
        url = reverse('todo-detail', kwargs={'pk': 2})
        self.client.force_authenticate(self.user)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_response_no_content_data(self):
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.url)
        self.assertEqual(response.data, None)

    def test_delete_response_header_allow_delete(self):
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.url)
        self.assertTrue('DELETE' in response.headers['allow'])
