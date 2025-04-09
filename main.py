#!/usr/bin/env python3
"""
Archivo principal para ejecutar el análisis de similitud de ArchivosTXT_Videojuegos.
"""

import os
from src.preprocessing import process_documents
from src.hash_utils import create_hash_tables, compare_documents
from src.sorting import merge_sort, show_top_results
from src.visualization import graph_similarity_results

def main():
    # Obtener la ruta raíz del proyecto (donde se encuentra main.py)
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # Definir la ruta de la carpeta de ArchivosTXT_Videojuegos en función del proyecto
    folder_path = os.path.join(project_root, "ArchivosTXT_Videojuegos")
    
    # Parámetros de procesamiento
    ngram_size = 3  # Tamaño de n-gramas (2 para bi-gramas, 3 para tri-gramas, etc.)
    top_n = 50      # Número de pares a mostrar
    
    # Paso 1 y 2: Cargar, limpiar y tokenizar ArchivosTXT_Videojuegos en n-gramas
    documents_data = process_documents(folder_path, ngram_size)
    if not documents_data:
        print('No se procesaron ArchivosTXT_Videojuegos.')
        return

    # Paso 3: Crear tablas hash con los n-gramas de cada documento
    hash_tables = create_hash_tables(documents_data)
    
    # Paso 4: Comparar ArchivosTXT_Videojuegos y calcular la similitud de Jaccard
    similarity_results = compare_documents(hash_tables)
    
    # Paso 5: Ordenar los resultados (orden descendente) usando Merge Sort
    sorted_results = merge_sort(similarity_results)
    
    # Paso 6: Mostrar los top N pares de ArchivosTXT_Videojuegos más similares en consola
    show_top_results(sorted_results, top_n)
    
    # Funcionalidad adicional: Graficar los resultados y guardarlos en la carpeta "resultados"
    save_path = os.path.join(project_root, "resultados", "similarity_results.png")
    graph_similarity_results(sorted_results, top_n, save_path=save_path)

if __name__ == '__main__':
    main()
