# Proyecto de Detección de Similitud entre Documentos

## Descripción general
El objetivo de este programa es comparar los documentos estudiantiles y detectar si hay plagio.
Este sistema utiliza tablas hash para almacenar y comparar los documentos según su similitud.
Este proyecto tokeniza documentos en n-gramas, utiliza funciones hash (y opcionalmente filtros de Bloom) para mapear los n-gramas, compara documentos utilizando la similitud de Jaccard y ordena los resultados con un algoritmo de ordenamiento (Merge Sort). Finalmente, muestra los N pares de documentos con mayor similitud.

## Estructura del Proyecto
- **main.py**: Archivo principal de ejecución.
- **src/**: Contiene módulos reutilizables:
  - `preprocessing.py`: Funciones de preprocesamiento de texto y generación de n-gramas.
  - `hash_utils.py`: Funciones hash personalizadas y comparación de documentos.
  - `sorting.py`: Implementación de Merge Sort y visualización de resultados.
  - `bloom_filter.py`: (Opcional) Implementación de un filtro de Bloom.
- **documentos/**: Carpeta donde se colocan los archivos .txt (trabajos estudiantiles).
- **resultados/**: Carpeta para guardar los resultados generados.
- **tests/**: Casos de prueba y archivos de validación.


Instrucciones de instalación:
-Clonarlo del repositorio en github
-Instalar lo

Ejemplo de uso: