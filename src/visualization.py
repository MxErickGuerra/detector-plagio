import os
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def graph_similarity_results(results, top_n, save_path="resultados/similarity_results.png"):
    """
    Grafica SOLO los top N documentos como nodos, con conexiones solo para los top N pares.
    """
    # Crear un grafo vacío
    G = nx.Graph()

    # Obtener solo los top N resultados
    top_results = results[:top_n]

    # Añadir los nodos y las conexiones para los top N resultados
    for res in top_results:
        doc_a = res['fileA']
        doc_b = res['fileB']
        sim = res['similarity'] * 10
        G.add_node(doc_a)
        G.add_node(doc_b)
        G.add_edge(doc_a, doc_b, weight=sim)

    # Obtener el layout de Fruchterman-Reingold (spring layout)
    pos = nx.spring_layout(G, k=1.5, iterations=100, seed=42)

    plt.figure(figsize=(30, 30))  # Ampliar el tamaño de la figura

    # Dibujar nodos con colores más suaves
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='#b2ebf2', alpha=0.9)

    # Dibujar etiquetas de los nodos
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

    # Dibujar las conexiones (aristas) con grosor proporcional a la similitud
    edges = G.edges(data=True)
    edge_widths = [0.5 + (data['weight'] / 30) for _, _, data in edges]
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=edge_widths, alpha=0.7, edge_color='#9575cd')

    # Agregar etiquetas de similitud en las conexiones
    for (doc_a, doc_b, data) in edges:
        sim = data['weight']
        x1, y1 = pos[doc_a]
        x2, y2 = pos[doc_b]

        # Posición intermedia para la etiqueta
        mid_x = (x1 + x2) * 0.5
        mid_y = (y1 + y2) * 0.5

        plt.text(mid_x, mid_y, f'{sim:.1f}%', fontsize=10, ha='center', va='center', color='black',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    plt.title(f'Red de documentos: {len(G.nodes)} archivos analizados\n(Líneas muestran top {top_n} conexiones)', pad=20)
    plt.axis('off')

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, bbox_inches='tight', dpi=120)
    print(f"Gráfico guardado en: {save_path}")
    plt.show()
