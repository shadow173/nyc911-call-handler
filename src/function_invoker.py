
from src.api_functions import function_a, function_b  # , ..., function_j

FUNCTION_MAP = {
    'FunctionA': function_a,
    'FunctionB': function_b,
    # Add mappings for all functions
}

def invoke_function(function_name):
    function = FUNCTION_MAP.get(function_name)
    if function:
        return function()
    else:
        raise ValueError(f"Function {function_name} is not recognized.")
