import sys
import os

# Agregar la ruta raíz del proyecto (un nivel arriba de la carpeta tests) a sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import unittest
from src.sorting import merge_sort

class TestSorting(unittest.TestCase):

    def test_merge_sort(self):
        # Prueba: ordenar una lista de diccionarios por la clave 'similarity' de forma descendente.
        data = [
            {"fileA": "a", "fileB": "b", "similarity": 0.4},
            {"fileA": "a", "fileB": "c", "similarity": 0.8},
            {"fileA": "b", "fileB": "c", "similarity": 0.1},
            {"fileA": "a", "fileB": "d", "similarity": 0.9},
        ]
        sorted_data = merge_sort(data)
        # El primer elemento debe tener la mayor similitud
        self.assertEqual(sorted_data[0]["similarity"], 0.9)
        # El último debe tener la menor similitud
        self.assertEqual(sorted_data[-1]["similarity"], 0.1)
    
    def test_merge_sort_more_elements(self):
        # Prueba: ordenar una lista más grande de diccionarios.
        data = [
            {"fileA": "a", "fileB": "b", "similarity": 0.4},
            {"fileA": "a", "fileB": "c", "similarity": 0.8},
            {"fileA": "b", "fileB": "c", "similarity": 0.1},
            {"fileA": "a", "fileB": "d", "similarity": 0.9},
            {"fileA": "c", "fileB": "d", "similarity": 0.5},
            {"fileA": "b", "fileB": "d", "similarity": 0.7},
        ]
        sorted_data = merge_sort(data)
        self.assertEqual(sorted_data[0]["similarity"], 0.9)
        self.assertEqual(sorted_data[-1]["similarity"], 0.1)

    def test_merge_sort_empty(self):
        # Prueba: verificar el caso de lista vacía.
        data = []
        sorted_data = merge_sort(data)
        self.assertEqual(sorted_data, [])

    def test_merge_sort_single_element(self):
        # Prueba: verificar que una lista con un solo elemento no se vea alterada.
        data = [{"fileA": "a", "fileB": "b", "similarity": 0.4}]
        sorted_data = merge_sort(data)
        self.assertEqual(sorted_data, data)

    def test_merge_sort_duplicate_similarities(self):
        # Prueba: verificar cómo se maneja la lista con elementos de similitud duplicada.
        data = [
            {"fileA": "a", "fileB": "b", "similarity": 0.8},
            {"fileA": "c", "fileB": "d", "similarity": 0.8},
            {"fileA": "e", "fileB": "f", "similarity": 0.8},
        ]
        sorted_data = merge_sort(data)
        # El orden no debe cambiar porque todos tienen la misma similitud.
        self.assertEqual(sorted_data, data)
       

if __name__ == "__main__":
    unittest.main()
