""" 
This file is responsible for visualizing the circuit and its optimization process. It could generate graphs or visual representations of the circuit's layout, components, and connections.

Tasks:

Visualize Circuit: Create visual representations (e.g., graphs or diagrams) to help understand the circuit's layout and connections.
Visualize Optimization: Show before-and-after views of the circuit to demonstrate how optimization has improved it.
"""
import networkx as nx
import matplotlib.pyplot as plt
import json

def visualize_circuit(circuit):
    G = nx.DiGraph()  # Use directed graph for logic flow
    with open('data/circuit_data.json') as f:
        circuit_data = json.load(f)
    # Check if components are stored as strings or objects
    
    for component in circuit.components:
        if isinstance(component, str):
            componentname = None
            for c in circuit_data['components']:
                if c['id'] == component:
                    componentname = c['type']
            G.add_node(component, label=componentname + "ON")  # If component is a string, use it as an ID
        else:
            G.add_node(component.id, label=f"{component.component_type} (ID: {component.id})")

    # Add edges based on connections
    for connection in circuit.connections:
         G.add_edge(connection[0], connection[1])  # Access tuple elements by index

    # Use a spring layout for visualization
    pos = nx.spring_layout(G, seed=42)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightblue", alpha=0.9)
    nx.draw_networkx_edges(G, pos, width=2, edge_color="black", alpha=0.7)
    nx.draw_networkx_labels(
        G, pos, labels=nx.get_node_attributes(G, "label"), font_size=10, font_color="black"
    )

    # Add title and display the graph
    plt.title("Logic Gate Circuit Visualization", fontsize=14)
    plt.axis("off")
    plt.show()
