""" 
in this file we will parse the circuit input
i will use the json data to parse the circuit

Tasks:

Read Input Data: Load the JSON file containing circuit information (components and connections).
Create Objects: Instantiate Python objects for each component (e.g., resistors, capacitors) and connection (e.g., how components are wired together).
Return a Circuit Object: Return a structured representation of the circuit (a Circuit object) that other modules can interact with.
"""
from .component import Component
from .circuit import Circuit

def parse_circuit(json_data):
    circuit = Circuit()
    
    # Parse components (logic gates)
    for component_data in json_data['components']:
        component = Component(
            component_data['type'],  # Logic gate type (AND, OR, etc.)
            component_data['id']
        )
        circuit.add_component(component)

    # Parse connections
    for connection in json_data['connections']:
        component1 = circuit.get_component_by_id(connection['from'])
        component2 = circuit.get_component_by_id(connection['to'])
        circuit.connect_components(component1, component2)

    return circuit
