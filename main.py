""" 
this is the entry point from the program

Responsibilities of main.py:
Import the necessary modules.
Parse command-line arguments to allow users to specify input files, optimization parameters, etc.
Load the circuit data from the specified file.
Optimize the circuit using the optimizer module.
Simulate the circuit to compute values like power, voltage, etc.
Visualize the circuit (optional, based on the design).
Display the results in the terminal or save them to a file.
"""

from src.parser import parse_circuit
from src.visualizer import visualize_circuit
from src.simulator import simulate
import json

def main():
    with open('data/circuit_data.json') as f:
        circuit_data = json.load(f)
    
    circuit = parse_circuit(circuit_data)
    outputs = simulate(circuit, circuit_data['initial_inputs'])
    print("Final Outputs:", outputs)
    
    visualize_circuit(circuit)

if __name__ == "__main__":
    main()

