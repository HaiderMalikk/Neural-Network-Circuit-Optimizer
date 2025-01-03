""" 
this component.py file to define the structure of circuit components (like resistors, capacitors, etc.).

Tasks:

Define Component Class: Each component (resistor, capacitor, etc.) will be an instance of the Component class.
Define Properties: Each component will have properties like type, value, and id.
"""

class Component:
    def __init__(self, component_type, id):
        self.component_type = component_type  # E.g., 'AND', 'OR', 'NOT', etc.
        self.id = id  # Unique identifier for the component
        self.connections = []  # List of other components connected to this one

    def add_connection(self, component):
        self.connections.append(component)

    def __str__(self):
        return f"{self.component_type} (ID: {self.id})"

