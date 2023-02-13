from django.test import TestCase
from todo.models import TEXT_MAX_LENGTH, TodoItem


class TodoItemTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo_item = TodoItem(title='title')

    def test_has_title(self):
        has_title = hasattr(self.todo_item, 'title')
        self.assertTrue(has_title)   
    
    def test_title_max_length_is_255(self):
        title_max_length = self.todo_item._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 255)
    
    def test_text_const_is_255(self):
        self.assertEqual(TEXT_MAX_LENGTH, 255)

    def test_has_description(self):
        has_description = hasattr(self.todo_item, 'description')
        self.assertTrue(has_description)
    
    def test_has_done(self):
        has_done = hasattr(self.todo_item, 'done')
        self.assertTrue(has_done)

    def test_done_default_is_false(self):
        done_default = self.todo_item._meta.get_field('done').default
        self.assertFalse(done_default)

    def test_has_created_at(self):
        has_created_at = hasattr(self.todo_item, 'created_at')
        self.assertTrue(has_created_at)

    def test_created_at_set_now_first_time_created(self):
        set_now_first_time_created = self.todo_item._meta.get_field('created_at').auto_now_add
        self.assertTrue(set_now_first_time_created)

    def test_has_updated_at(self):
        has_updated_at = hasattr(self.todo_item, 'updated_at')
        self.assertTrue(has_updated_at) 

    def test_updated_at_set_now_every_time_saved(self):
        set_now_every_time_saved = self.todo_item._meta.get_field('updated_at').auto_now
        self.assertTrue(set_now_every_time_saved)

    def test_task_string_representation(self):
        self.assertEqual(str(self.todo_item),'title')


   


