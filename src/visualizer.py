""" 
This file is responsible for visualizing the circuit and its optimization process. It could generate graphs or visual representations of the circuit's layout, components, and connections.

Tasks:

Visualize Circuit: Create visual representations (e.g., graphs or diagrams) to help understand the circuit's layout and connections.
Visualize Optimization: Show before-and-after views of the circuit to demonstrate how optimization has improved it.
"""

import networkx as nx
import matplotlib.pyplot as plt

def visualize_circuit(circuit):
    G = nx.Graph()

    # Add nodes with labels for each component
    for component in circuit.components:
        G.add_node(component.id, label=f"{component.component_type} ({component.value} Ohms)")

    # Connect components sequentially
    for i in range(len(circuit.components) - 1):
        G.add_edge(circuit.components[i].id, circuit.components[i + 1].id)

    # Use a spring layout for positioning
    pos = nx.spring_layout(G, seed=42)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightblue", alpha=0.9)
    nx.draw_networkx_edges(G, pos, width=2, edge_color="black", alpha=0.7)
    nx.draw_networkx_labels(
        G, pos, labels=nx.get_node_attributes(G, "label"), font_size=10, font_color="black"
    )

    # Add title and show the plot
    plt.title("Circuit Visualization - Optimized", fontsize=14)
    plt.axis("off")
    plt.show()
