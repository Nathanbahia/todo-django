from django.test import TestCase
from django.urls import resolve
from .views import index, remove, edit
from .models import TaskModel

# python manage.py test

class TestIndex(TestCase):
    def test_path_index_view(self):
        path = resolve('/')
        self.assertEqual(path.func, index)


    def test_render_html_index_view(self):
        response = self.client.get('/')
        template = 'index.html'
        self.assertTemplateUsed(response, template)


class TestRemove(TestCase):
    def test_path_remove_view(self):
        path = resolve('/remove/1')
        self.assertEqual(path.func, remove)


    def test_remove_item(self):
        new_task = TaskModel(text='This is a unit test example')
        new_task.save()

        task = TaskModel.objects.get(text='This is a unit test example')                
        task.active = False
        task.save()
        self.assertEqual(task.active, False)


class TestEdit(TestCase):
    def test_path_edit_view(self):
        path = resolve('/edit/1')
        self.assertEqual(path.func, edit)


class TestTaskModel(TestCase):
    def test_save_task(self):
        response = self.client.post('/', data={'text': 'A new list item'})
        self.assertEqual(TaskModel.objects.count(), 1)
        
        new_item = TaskModel.objects.first()
        self.assertEqual(new_item.text, 'A new list item')         
        
        
