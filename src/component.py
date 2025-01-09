""" 
this component.py file to define the structure of circuit components (like resistors, capacitors, etc.).

Tasks:

Define Component Class: Each component (resistor, capacitor, etc.) will be an instance of the Component class.
Define Properties: Each component will have properties like type, value, and id.
"""
# component.py
# component.py
inputdict = {}
class Component:
    def __init__(self, component_type, id):  
        self.component_type = component_type  # E.g., 'AND', 'OR', 'NOT'
        self.id = id  # Unique identifier for the component
        self.connections = []  # Connected components
        self.inputs = []  # Dynamic input storage

    def add_connection(self, component):
        self.connections.append(component)

    def evaluate(self):
        inputdict[self.id] = self.inputs # add input to corresponding id
        from src.logic_functions import get_logic_function
        if self.component_type == "NOT" and len(self.inputs) != 1: # not gate only has 1 input
            raise ValueError(f"NOT gate {self.id} must have exactly one input.")
        logic_func = get_logic_function(self.component_type)
        return logic_func(self.inputs) if self.inputs else 0  # Default to 0

    def __str__(self):
        return f"{self.component_type} (ID: {self.id})"