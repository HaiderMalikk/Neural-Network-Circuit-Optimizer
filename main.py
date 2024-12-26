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
import json

def main():
    # Load the circuit data
    with open('data/circuit_data.json') as f:
        circuit_data = json.load(f)

    # Parse the circuit
    circuit = parse_circuit(circuit_data)

    visualize_circuit(circuit)

if __name__ == "__main__":
    main()
