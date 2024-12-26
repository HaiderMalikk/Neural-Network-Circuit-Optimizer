""" 
Circuit class, which represents the entire circuit that im working with in my project. The Circuit class is where i would store all the components and their connections, 
essentially managing the whole structure of the circuit.

The Purpose of the Circuit Class:
The Circuit class acts as a container for all the components (resistors, capacitors, etc.) and their connections.
You can add, remove, and manage components within the circuit, and it allows you to store information like component values, types, and their relationships 
(e.g., which component is connected to which).
"""


class Circuit:
    def __init__(self):
        self.components = []  # List of all components in the circuit
        self.connections = []  # List of connections (edges between components)

    def add_component(self, component):
        self.components.append(component)

    def connect_components(self, component1, component2):
        # Connect two components
        component1.add_connection(component2)
        component2.add_connection(component1)
        self.connections.append((component1, component2))

    def get_component_by_id(self, component_id):
        # Retrieve a component by its unique ID
        for component in self.components:
            if component.id == component_id:
                return component
        raise ValueError(f"Component with ID {component_id} not found.")

    def __str__(self):
        return f"Circuit with {len(self.components)} components and {len(self.connections)} connections."

