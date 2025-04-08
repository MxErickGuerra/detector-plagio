import os
import matplotlib.pyplot as plt
import numpy as np

def graph_similarity_results(results, top_n, save_path="resultados/similarity_results.png"):
    """
    Grafica TODOS los documentos como nodos, con conexiones solo para los top N pares.
    """
    # Obtener TODOS los documentos únicos de todos los resultados (no solo top N)
    all_docs = set()
    for res in results:
        all_docs.add(res['fileA'])
        all_docs.add(res['fileB'])
    unique_docs = list(all_docs)
    
    # Layout circular para todos los nodos
    n = len(unique_docs)
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(angles) * 2.5
    y = np.sin(angles) * 2.5
    pos = {doc: (xi, yi) for doc, xi, yi in zip(unique_docs, x, y)}
    
    plt.figure(figsize=(20, 20))
    
    # Dibujar TODOS los nodos (incluso sin conexiones)
    for doc, (xi, yi) in pos.items():
        plt.plot(xi, yi, 'o', markersize=14, color='#b2ebf2', alpha=0.9)
        plt.text(xi, yi, doc, 
                fontsize=9, 
                ha='center', 
                va='bottom', 
                weight='bold',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))
    
    # Dibujar solo las conexiones del top N
    top_results = results[:top_n]
    for res in top_results:
        doc_a = res['fileA']
        doc_b = res['fileB']
        sim = res['similarity'] * 100
        
        x1, y1 = pos[doc_a]
        x2, y2 = pos[doc_b]
        
        # Grosor de línea proporcional a la similitud
        linewidth = 0.5 + (sim / 30)
        plt.plot([x1, x2], [y1, y2], 
                color='#9575cd', 
                linestyle='-', 
                alpha=0.6,
                linewidth=linewidth)
        
        # Etiqueta de porcentaje
        mid_x = (x1 + x2)*0.5
        mid_y = (y1 + y2)*0.5
        plt.text(mid_x, mid_y, f'{sim:.1f}%', 
                fontsize=8,
                ha='center', 
                va='center', 
                color='#000000',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    plt.title(f'Red de documentos: {len(unique_docs)} archivos analizados\n(Líneas muestran top {top_n} conexiones)', pad=20)
    plt.axis('off')
    
    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, bbox_inches='tight', dpi=120)
    print(f"Gráfico guardado en: {save_path}")
    plt.show()
