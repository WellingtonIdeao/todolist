from django.test import TestCase
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskSerializerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.task_attributes = {
            'title': 'title',
            'description': 'description',
            'done': False,
            'created_at':'2022-12-03',
            'updated_at': '2022-12-03' 
        }
        cls.task = Task(**cls.task_attributes)
        cls.serializer = TaskSerializer(instance=cls.task)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data    
        self.assertCountEqual(
            set(data.keys()),
            set(['title', 'description', 'done', 'created_at', 'updated_at'])
        )

    def test_title_field_content(self):
        data = self.serializer.data    
        self.assertEqual(data['title'], self.task_attributes['title'])

    def test_description_field_content(self):
        data = self.serializer.data    
        self.assertEqual(data['description'], self.task_attributes['description']) 

    def test_done_field_content(self):
        data = self.serializer.data    
        self.assertEqual(data['done'], self.task_attributes['done'])

    def test_created_at_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['created_at'], self.task_attributes['created_at'])                  

    def test_updated_at_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['updated_at'], self.task_attributes['updated_at'])  

