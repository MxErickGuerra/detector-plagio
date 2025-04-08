#!/usr/bin/env python3
"""
Archivo principal para ejecutar el análisis de similitud de documentos.
"""

from src.preprocessing import process_documents
from src.hash_utils import create_hash_tables, compare_documents
from src.sorting import merge_sort, show_top_results
from src.visualization import graph_similarity_results

def main():
    folder_path = './documentos'  # Carpeta con los archivos .txt
    ngram_size = 3                # Tamaño de n-gramas: 2 para bi-gramas, 3 para tri-gramas, etc.
    top_n = 6                     # Número de pares a mostrar

    # Procesar documentos
    documents_data = process_documents(folder_path, ngram_size)
    if not documents_data:
        print('No se procesaron documentos.')
        return

    # Crear tablas hash con los n-gramas de cada documento
    hash_tables = create_hash_tables(documents_data)

    # Comparar cada par de documentos y calcular similitud Jaccard
    similarity_results = compare_documents(hash_tables)

    # Ordenar los resultados (descendente) con merge sort
    sorted_results = merge_sort(similarity_results)

    # Mostrar resultados en consola
    show_top_results(sorted_results, top_n)

    # Graficar y guardar los resultados en la carpeta 'resultados'
    graph_similarity_results(sorted_results, top_n, save_path="resultados/similarity_results.png")

if __name__ == '__main__':
    main()
