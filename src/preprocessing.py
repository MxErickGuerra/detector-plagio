"""
Módulo de preprocesamiento de texto.
Contiene funciones para limpiar el texto, generar n-gramas y procesar documentos.
"""

import os
import re

def clean_text(text):
    """
    Limpia el texto: lo pasa a minúsculas, elimina signos de puntuación y espacios extra.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Quita la puntuación
    text = re.sub(r'\s+', ' ', text).strip()  # Reemplaza múltiples espacios con uno solo y quita espacios extra
    return text

def generate_ngrams(text, n):
    """
    Tokeniza el texto en n-gramas.
    """
    words = text.split()
    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(' '.join(words[i:i+n]))
    return ngrams

def process_documents(folder_path, ngram_size):
    """
    Procesa todos los documentos de texto en la carpeta especificada.
    Para cada documento:
      - Lee el archivo.
      - Limpia el texto.
      - Genera n-gramas.
    
    Retorna un diccionario con la siguiente estructura:
      {
         'archivo.txt': {
             'original_text': <texto original>,
             'cleaned_text': <texto limpio>,
             'ngrams': [lista de n-gramas],
             'ngram_count': <cantidad de n-gramas>
         },
         ...
      }
    """
    documents_data = {}

    # Paso 1: Crear el folder si no existe
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f'Folder "{folder_path}" fue creado o ya existe.')
    except Exception as e:
        print(f'Error al crear folder: {e}')
        return {}

    # Listar archivos y filtrar los archivos .txt
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        print(f'Error al listar archivos en {folder_path}: {e}')
        return {}

    text_files = [file for file in files if os.path.splitext(file)[1].lower() == '.txt']

    if not text_files:
        print('No se encontraron archivos de texto en el folder. Añade algunos archivos .txt')
        return {}

    print(f'Se encontraron {len(text_files)} archivos de texto.')

    # Procesar cada archivo
    for file in text_files:
        file_path = os.path.join(folder_path, file)
        try:
            with open(file_path, 'r', encoding='utf8') as f:
                content = f.read()
        except Exception as e:
            print(f'Error al leer el archivo {file}: {e}')
            continue

        cleaned_text = clean_text(content)
        ngrams = generate_ngrams(cleaned_text, ngram_size)
        documents_data[file] = {
            'original_text': content,
            'cleaned_text': cleaned_text,
            'ngrams': ngrams,
            'ngram_count': len(ngrams)
        }
        print(f'Procesando "{file}": {len(ngrams)} {ngram_size}-gramas generados.')

    return documents_data
