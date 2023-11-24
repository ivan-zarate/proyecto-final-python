from django.test import TestCase

from .models import Notebooks
from django.urls import reverse

class EliminarNotebookTest(TestCase):
    def setUp(cls):
        Notebooks.objects.create(nombre="Notebook1", precio=587485, cantidad=45)

    def test_nombre(self):
        notebook=Notebooks.objects.get(id=1)
        field_label = notebook._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre')
        self.assertQuerysetEqual(Notebooks.objects.all())
