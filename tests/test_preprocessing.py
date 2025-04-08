import sys
import os

# Agregar la ruta raíz del proyecto (un nivel arriba de la carpeta tests) a sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import unittest
from src.preprocessing import clean_text, generate_ngrams

class TestPreprocessing(unittest.TestCase):
    def test_clean_text(self):
        # Prueba: se debe convertir el texto a minúsculas, eliminar puntuación y espacios adicionales.
        text = "Hola, MUNDO!  Esto es una prueba."
        expected = "hola mundo esto es una prueba"
        result = clean_text(text)
        self.assertEqual(result, expected)

    def test_generate_ngrams(self):
        # Prueba: se deben generar correctamente los n-gramas a partir del texto.
        text = "hola mundo esto es una prueba"
        n = 2
        expected = ["hola mundo", "mundo esto", "esto es", "es una", "una prueba"]
        result = generate_ngrams(text, n)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
