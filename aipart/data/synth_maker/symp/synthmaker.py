import sympy as sp
from sympy import preview

# Define symbols
x = sp.symbols('x')

# Create an expression
expr = sp.sin(x) * sp.exp(x)

# Save the expression to a PNG file
preview(expr, output='png', filename='expression.png', dvioptions=['-D', '600'])
