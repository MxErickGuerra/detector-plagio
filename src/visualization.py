import os
import matplotlib.pyplot as plt

def graph_similarity_results(results, top_n, save_path="resultados/similarity_results.png"):
    """
    Grafica los resultados de similitud entre documentos y guarda la imagen en la carpeta 'resultados'.

    :param results: Lista ordenada de diccionarios con la estructura:
                    {'fileA': <nombre_archivo1>, 'fileB': <nombre_archivo2>, 'similarity': <valor>}
    :param top_n: Número de pares de documentos a graficar
    :param save_path: Ruta del archivo donde se guardará el gráfico
    """
    # Selecciona los top N resultados
    top_results = results[:top_n]
    
    # Prepara las etiquetas y los valores (como porcentajes)
    labels = [f"{r['fileA']} \n<->\n {r['fileB']}" for r in top_results]
    similarities = [r['similarity'] * 100 for r in top_results]  # Convertir similitud a porcentaje
    
    # Configura la figura y realiza la gráfica de barras
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, similarities, color='skyblue')
    plt.xlabel('Pares de Documentos')
    plt.ylabel('Similitud (%)')
    plt.title(f'Top {top_n} Pares de Documentos Más Similares')
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 100)

    # Agregar el valor de la similitud sobre cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.1f}%', 
                 ha='center', va='bottom')

    plt.tight_layout()

    # Crear la carpeta 'resultados' si no existe
    output_folder = os.path.dirname(save_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Guardar el gráfico en la carpeta 'resultados'
    plt.savefig(save_path)
    print(f"Gráfico guardado en: {save_path}")

    # Mostrar el gráfico
    plt.show()
