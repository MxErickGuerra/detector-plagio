import sys
import os

# Agregar la ruta raíz del proyecto (un nivel arriba de la carpeta tests) a sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import unittest
from src.hash_utils import simple_hash, jaccard_similarity, create_hash_tables, compare_documents

class TestHashUtils(unittest.TestCase):
    def test_simple_hash(self):
        # Prueba: La misma cadena debe producir el mismo valor hash.
        s = "hola mundo"
        h1 = simple_hash(s)
        h2 = simple_hash(s)
        self.assertEqual(h1, h2)
        self.assertIsInstance(h1, int)

    def test_jaccard_similarity(self):
        # Prueba: calcular la similitud de Jaccard para dos conjuntos.
        set_a = {1, 2, 3}
        set_b = {2, 3, 4}
        expected = 2 / 4  # La intersección tiene 2 elementos, la unión 4 elementos.
        result = jaccard_similarity(set_a, set_b)
        self.assertAlmostEqual(result, expected)

    def test_create_and_compare_documents(self):
        # Prueba: creación de tablas hash y comparación de documentos.
        documents_data = {
            "doc1.txt": {"ngrams": ["hola mundo", "mundo esto"]},
            "doc2.txt": {"ngrams": ["mundo esto", "esto es"]}
        }
        hash_tables = create_hash_tables(documents_data)
        self.assertIn("doc1.txt", hash_tables)
        self.assertIn("doc2.txt", hash_tables)
        
        results = compare_documents(hash_tables)
        # Con dos documentos, debe haber un único resultado de comparación.
        self.assertEqual(len(results), 1)
        # La similitud debe estar entre 0 y 1.
        self.assertGreaterEqual(results[0]["similarity"], 0.0)
        self.assertLessEqual(results[0]["similarity"], 1.0)

if __name__ == "__main__":
    unittest.main()
