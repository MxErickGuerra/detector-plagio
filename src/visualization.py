import os
import matplotlib.pyplot as plt
import numpy as np

def graph_similarity_results(results, top_n, save_path="resultados/similarity_results.png"):
    """
    Grafica los resultados de similitud como una red de documentos conectados,
    con líneas que muestran el porcentaje de similitud.
    """
    top_results = results[:top_n]
    
    # Recopilar documentos únicos
    unique_docs = set()
    for res in top_results:
        unique_docs.add(res['fileA'])
        unique_docs.add(res['fileB'])
    unique_docs = list(unique_docs)
    
    # Crear un layout circular para los nodos
    n = len(unique_docs)
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)
    pos = {doc: (xi, yi) for doc, xi, yi in zip(unique_docs, x, y)}
    
    plt.figure(figsize=(10, 10))
    
    # Dibujar nodos
    for doc, (xi, yi) in pos.items():
        plt.plot(xi, yi, 'o', markersize=12, color='skyblue', alpha=0.6)
        plt.text(xi, yi, doc, fontsize=9, ha='center', va='bottom', weight='bold')
    
    # Dibujar conexiones con porcentajes
    for res in top_results:
        doc_a = res['fileA']
        doc_b = res['fileB']
        sim = res['similarity'] * 100
        
        x1, y1 = pos[doc_a]
        x2, y2 = pos[doc_b]
        
        # Línea de conexión
        plt.plot([x1, x2], [y1, y2], color='gray', linestyle='--', alpha=0.4)
        
        # Etiqueta de porcentaje
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        plt.text(mid_x, mid_y, f'{sim:.1f}%', 
                 fontsize=9, ha='center', va='center',
                 bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.2'))
    
    plt.title(f'Conexiones de similitud entre documentos (Top {top_n})', pad=20)
    plt.axis('off')
    
    # Asegurar carpeta de resultados
    output_folder = os.path.dirname(save_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    plt.savefig(save_path, bbox_inches='tight')
    print(f"Gráfico de red guardado en: {save_path}")
    plt.show()
