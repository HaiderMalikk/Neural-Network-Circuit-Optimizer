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
    for comp in json_data['components']:
        circuit.add_component(Component(comp['type'], comp['id']))
    
    for conn in json_data['connections']:
        circuit.connect_components(conn['from'], conn['to'])
    
    return circuit
