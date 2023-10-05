import sympy as sp

# Define symbolic variables
t1, t2, t3, t4 = sp.symbols('t1 t2 t3 t4')

# Define the skew-symmetric matrices, now using the sympy notation instead of numpy
z_hat_bracket = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
y_hat_bracket = sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])

# Calculate e_bracket_z_t1, now using the sympy notation instead of numpy
e_bracket_z_t1 = sp.eye(3) + sp.sin(t1)*z_hat_bracket + (1 - sp.cos(t1))*(z_hat_bracket @ z_hat_bracket)

# Calculate e_bracket_y_t2
e_bracket_y_t2 = sp.eye(3) + sp.sin(t2)*y_hat_bracket + (1 - sp.cos(t2))*(y_hat_bracket @ y_hat_bracket)

# Calculate e_bracket_y_t3
e_bracket_y_t3 = sp.eye(3) + sp.sin(t3)*y_hat_bracket + (1 - sp.cos(t3))*(y_hat_bracket @ y_hat_bracket)

# Calculate e_bracket_y_t4
e_bracket_y_t4 = sp.eye(3) + sp.sin(t4)*y_hat_bracket + (1 - sp.cos(t4))*(y_hat_bracket @ y_hat_bracket)

# Calculate the final result
result = e_bracket_z_t1 @ e_bracket_y_t2 @ e_bracket_y_t3 @ e_bracket_y_t4

# Simplify the result
simplified_result = sp.simplify(result)

# Display the simplified result with the appropriate sympy print command
sp.pprint(simplified_result)