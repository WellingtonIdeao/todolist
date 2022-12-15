from django.test import TestCase
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer

class TodoItemSerializerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo_item_attributes = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'created_at':'2022-12-03',
            'updated_at': '2022-12-03' 
        }
        cls.todo_item = TodoItem(**cls.todo_item_attributes)
        cls.serializer = TodoItemSerializer(instance=cls.todo_item)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data    
        self.assertCountEqual(
            set(data.keys()),
            set(['title', 'description', 'done', 'created_at', 'updated_at'])
        )

    def test_title_field_content(self):
        data = self.serializer.data    
        self.assertEqual(data['title'], self.todo_item_attributes['title'])

    def test_description_field_content(self):
        data = self.serializer.data    
        self.assertEqual(data['description'], self.todo_item_attributes['description']) 

    def test_done_field_content(self):
        data = self.serializer.data    
        self.assertEqual(data['done'], self.todo_item_attributes['done'])

    def test_created_at_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['created_at'], self.todo_item_attributes['created_at'])                  

    def test_updated_at_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['updated_at'], self.todo_item_attributes['updated_at'])  

