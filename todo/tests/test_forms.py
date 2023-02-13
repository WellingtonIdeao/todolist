from django.test import TestCase

from todo.models import TodoItem


class TodoItemFormTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo_item = TodoItem(title='title')

    def test_title_label(self):
        title_label = self.todo_item._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_title_is_required(self):
        title_can_empty = self.todo_item._meta.get_field('title').blank
        self.assertFalse(title_can_empty)

    def test_description_label(self):
        desc_label = self.todo_item._meta.get_field('description').verbose_name
        self.assertEqual(desc_label, 'description')

    def test_description_is_required(self):
        desc_can_empty = self.todo_item._meta.get_field('description').blank
        self.assertFalse(desc_can_empty)

    def test_done_label(self):
        done_label = self.todo_item._meta.get_field('done').verbose_name
        self.assertEqual(done_label, 'done')

    def test_done_is_required(self):
        done_can_empty = self.todo_item._meta.get_field('done').blank
        self.assertFalse(done_can_empty)

    def test_created_at_label(self):
        created_at_label = self.todo_item._meta.get_field(
            'created_at').verbose_name
        self.assertEqual(created_at_label, 'createdAt')

    def test_updated_at_label(self):
        updated_at_label = self.todo_item._meta.get_field(
            'updated_at').verbose_name
        self.assertEqual(updated_at_label, 'updatedAt')
