""" 
Circuit class, which represents the entire circuit that im working with in my project. The Circuit class is where i would store all the components and their connections, 
essentially managing the whole structure of the circuit.

The Purpose of the Circuit Class:
The Circuit class acts as a container for all the components (resistors, capacitors, etc.) and their connections.
You can add, remove, and manage components within the circuit, and it allows you to store information like component values, types, and their relationships 
(e.g., which component is connected to which).
"""


# circuit.py
class Circuit:
    def __init__(self):
        self.components = {}
        self.connections = []

    def add_component(self, component):
        self.components[component.id] = component

    def connect_components(self, from_id, to_id):
        if from_id in self.components and to_id in self.components:
            self.components[from_id].add_connection(self.components[to_id])
            self.connections.append((from_id, to_id))
        else:
            raise ValueError("Invalid connection IDs.")

    def evaluate(self, initial_inputs):
        for comp_id, value in initial_inputs.items():
            if comp_id in self.components:
                self.components[comp_id].inputs = value
        
        outputs = {}
        for comp in self.components.values():
            outputs[comp.id] = comp.evaluate()
            for connected in comp.connections:
                connected.inputs.append(outputs[comp.id])
        
        return outputs
