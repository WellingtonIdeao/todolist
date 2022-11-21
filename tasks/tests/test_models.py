from django.test import TestCase
from ..models import Task, TEXT_MAX_LENGTH

class TaskModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(title='title')

    def test_has_title(self):
        has_title = hasattr(self.task, 'title')
        self.assertTrue(has_title)

    def test_title_label(self):
        title_label = self.task._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')    
    
    def test_title_max_length_is_255(self):
        title_max_length = self.task._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 255)
    
    def test_text_const_is_255(self):
        self.assertEqual(TEXT_MAX_LENGTH, 255)

    def test_title_is_required(self):
        title_can_empty = self.task._meta.get_field('title').blank
        self.assertFalse(title_can_empty)

    def test_has_description(self):
        has_description = hasattr(self.task, 'description')
        self.assertTrue(has_description)

    def test_description_label(self):
        desc_label = self.task._meta.get_field('description').verbose_name
        self.assertEqual(desc_label, 'description')         
    
    def test_description_is_required(self):
        desc_can_empty = self.task._meta.get_field('description').blank
        self.assertFalse(desc_can_empty)     

    def test_has_done(self):
        has_done = hasattr(self.task, 'done')
        self.assertTrue(has_done)

    def test_done_label(self):
        done_label = self.task._meta.get_field('done').verbose_name
        self.assertEqual(done_label, 'done')         
    
    def test_done_default_is_false(self):
        done_default = self.task._meta.get_field('done').default
        self.assertFalse(done_default)

    def test_has_created_at(self):
        has_created_at = hasattr(self.task, 'created_at')
        self.assertTrue(has_created_at)

    def test_created_at_label(self):
        created_at_label = self.task._meta.get_field('created_at').verbose_name
        self.assertEqual(created_at_label, 'createdAt')

    def test_created_at_set_now_first_time_created(self):
        set_now_first_time_created = self.task._meta.get_field('created_at').auto_now_add
        self.assertTrue(set_now_first_time_created)

    def test_has_updated_at(self):
        has_updated_at = hasattr(self.task, 'updated_at')
        self.assertTrue(has_updated_at) 
    
    def test_updated_at_label(self):
        updated_at_label = self.task._meta.get_field('updated_at').verbose_name
        self.assertEqual(updated_at_label, 'updatedAt')

    def test_updated_at_set_now_every_time_saved(self):
        set_now_every_time_saved = self.task._meta.get_field('updated_at').auto_now
        self.assertTrue(set_now_every_time_saved)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task),'title')


   


