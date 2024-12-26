def and_gate(inputs):
    """Simulate an AND gate."""
    return 1 if all(inputs) else 0

def or_gate(inputs):
    """Simulate an OR gate."""
    return 1 if any(inputs) else 0

def not_gate(inputs):
    """Simulate a NOT gate."""
    if len(inputs) != 1:
        raise ValueError("NOT gate expects exactly one input.")
    return 0 if inputs[0] == 1 else 1

def get_logic_function(gate_type):
    """Return the correct logic function based on the gate type."""
    if gate_type == "AND":
        return and_gate
    elif gate_type == "OR":
        return or_gate
    elif gate_type == "NOT":
        return not_gate
    else:
        raise ValueError(f"Unknown gate type: {gate_type}")
