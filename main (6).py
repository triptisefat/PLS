from dataclasses import dataclass
from typing import Union

@dataclass
class Constant:
    value: Union[int, float, bool]

# Example usage
int_constant = Constant(value=42)
float_constant = Constant(value=3.14)
bool_constant = Constant(value=True)

# Accessing and printing values
print(f"Integer Constant: {int_constant.value}")
print(f"Float Constant: {float_constant.value}")
print(f"Boolean Constant: {bool_constant.value}")
