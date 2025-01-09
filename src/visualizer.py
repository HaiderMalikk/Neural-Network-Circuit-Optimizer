""" 
This file is responsible for visualizing the circuit and its optimization process. It could generate graphs or visual representations of the circuit's layout, components, and connections.

Tasks:

Visualize Circuit: Create visual representations (e.g., graphs or diagrams) to help understand the circuit's layout and connections.
Visualize Optimization: Show before-and-after views of the circuit to demonstrate how optimization has improved it.
"""
import networkx as nx
import matplotlib.pyplot as plt
import json

def visualize_circuit(circuit, inputs, outputs):
    G = nx.DiGraph()  # Use directed graph for logic flow
    with open('data/circuit_data.json') as f:
        circuit_data = json.load(f)
    # Check if components are stored as strings or objects
    for component in circuit.components:
        componentname = None
        isinitial = ""
        for c in circuit_data['components']:
            if c['id'] == component:
                componentname = c['type']
        for i in circuit_data['initial_inputs']:
            if i == component:
                isinitial = "(Initial Input)\n"
        input = str(inputs[component])
        output = str(outputs[component]) 
        if output == "1":
            color = "green"
        elif output == "0":
            color = "red"
        else:
            color = "grey"
        
        # id, lable, color
        G.add_node(component, label= "id = " + component + "\n " + isinitial + componentname + " Gate\n Input: " + input + "\n Output: " +output, color=color)  # If component is a string, use it as an ID

    # Add edges based on connections
    for connection in circuit.connections:
         G.add_edge(connection[0], connection[1])  # Access tuple elements by index

    # Use a spring layout for visualization
    pos = nx.spring_layout(G, k = 1 ,seed=1) # k is the distance between nodes and seed is the random seed (both less to avoid overlapping)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    node_colors = [G.nodes[node]["color"] for node in G.nodes]  # Extract colors as a list
    nx.draw_networkx_nodes(G, pos, node_size=4000, node_color=node_colors, alpha=1.0)
    edge_colors = [G.nodes[edge[0]]["color"] for edge in G.edges]
    nx.draw_networkx_edges(G, pos, width=2, edge_color=edge_colors, alpha=1.0, arrowstyle="-|>", arrowsize=10, min_target_margin=30, min_source_margin=30)
    nx.draw_networkx_labels(
        G, pos, labels=nx.get_node_attributes(G, "label"), font_size=7, font_color="black"
    )
    # Add title and display the graph
    plt.title("Logic Gate Circuit Visualization", fontsize=14, pad=30)
    plt.text(0.5, 1, "Inputs: " + str(inputs) + "\nOutputs: " + str(outputs), ha="center", va="center", fontsize=8, transform=plt.gca().transAxes)
    plt.axis("off") 
    plt.show()
