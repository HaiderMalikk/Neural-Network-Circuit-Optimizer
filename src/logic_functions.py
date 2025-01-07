# logic_functions.py
def and_gate(inputs):
    return 1 if all(inputs) else 0

def or_gate(inputs):
    return 1 if any(inputs) else 0

def not_gate(inputs):
    if len(inputs) != 1:
        raise ValueError("NOT gate must have exactly one input.")
    return 0 if inputs[0] else 1

# final output gate is not a function but a array of outputs
def output(inputs): 
    return inputs

def get_logic_function(gate_type):
    return {"AND": and_gate, "OR": or_gate, "NOT": not_gate, "OUTPUT": output}.get(gate_type, lambda x: 0)
