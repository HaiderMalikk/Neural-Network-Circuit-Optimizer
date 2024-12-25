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
from src.optimizer import optimize_circuit
from src.simulator import simulate_circuit
from src.visualizer import visualize_circuit
import json

def main():
    with open('data/circuit_data.json') as f:
        circuit_data = json.load(f)

    # Parse circuit
    circuit = parse_circuit(circuit_data)

    # Optimize circuit
    optimized_circuit = optimize_circuit(circuit)

    # Simulate optimized circuit
    optimized_power = simulate_circuit(optimized_circuit)
    print(f"Optimized power consumption with a 5V supply: {optimized_power} W")

    # Visualize optimized circuit
    visualize_circuit(optimized_circuit)

if __name__ == "__main__":
    main()
