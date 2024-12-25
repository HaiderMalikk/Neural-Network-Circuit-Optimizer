""" 
This file is responsible for simulating the behavior of the circuit. The simulation could focus on power consumption, signal strength, or other performance metrics.

Tasks:

Simulate Circuit: Simulate how the circuit will behave based on the components and connections (e.g., calculate the power consumption, current flow, or voltage).
Return Simulation Results: Output the results of the simulation, such as power usage or any other relevant metric.
"""

import numpy as np

def simulate_circuit(circuit):
    # Extract resistances of all resistors
    resistors = [comp for comp in circuit.components if comp.component_type == "resistor"]
    if not resistors:
        raise ValueError("No resistors found in the circuit!")

    # Example: Assume a 5V source for simplicity
    voltage_source = 5  

    # Dynamically build resistance matrix and voltage vector
    num_resistors = len(resistors)
    R = np.zeros((num_resistors, num_resistors))  # Resistance matrix
    V = np.zeros(num_resistors)  # Voltage vector

    # Populate the resistance matrix and voltage vector
    for i, resistor in enumerate(resistors):
        R[i, i] = resistor.value  # Diagonal elements are the resistances
        if i < len(V):  # Ensure we don't exceed the size of V
            V[i] = voltage_source  # Assign the voltage source value

    # Solve for currents using Ohm's law: I = V/R
    try:
        currents = np.linalg.solve(R, V)
    except np.linalg.LinAlgError:
        raise ValueError("The resistance matrix is singular and cannot be solved!")

    # Calculate total power: P = V * I
    power = sum(V[i] * currents[i] for i in range(len(currents)))

    return power

