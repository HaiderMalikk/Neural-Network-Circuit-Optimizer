import pytest

from src.parser import parse_circuit
from src.simulator import simulate
from src.component import inputdict

# Mock circuit data (updated structure)
mock_circuit_data = {
    "components": [
        {"type": "NOT", "id": "G1"},
        {"type": "NOT", "id": "G2"},
        {"type": "AND", "id": "G3"},
        {"type": "NOT", "id": "G4"},
        {"type": "OR", "id": "G5"},
        {"type": "OUTPUT", "id": "OUT"}
    ],
    "connections": [
        {"from": "G1", "to": "G3"},
        {"from": "G2", "to": "G3"},
        {"from": "G3", "to": "G4"},
        {"from": "G4", "to": "G5"},
        {"from": "G4", "to": "OUT"},
        {"from": "G3", "to": "G5"},
        {"from": "G5", "to": "OUT"}
    ],
    "initial_inputs": {
        "G1": [0],
        "G2": [0]
    }
}

# Expected results
expected_inputdict = {
    "G1": [0],
    "G2": [0],
    "G3": [1, 1],
    "G4": [1],
    "G5": [1, 0],
    "OUT": [0, 1]
}

expected_outputs = {
    "G1": 1,
    "G2": 1,
    "G3": 1,
    "G4": 0,
    "G5": 1,
    "OUT": [0, 1]
}

def test_circuit_simulation():
    # Parse and simulate
    circuit = parse_circuit(mock_circuit_data)
    outputs = simulate(circuit, mock_circuit_data["initial_inputs"])

    # Assert input dictionary matches expected
    assert inputdict == expected_inputdict, f"Expected {expected_inputdict}, got {inputdict}"

    # Assert final outputs match expected
    assert outputs == expected_outputs, f"Expected {expected_outputs}, got {outputs}"
