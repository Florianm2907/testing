import scipy.optimize as opt

# Define the equation you want to solve
def equation(x):
    return (x * 343.51 / 4.905)**0.5 - 6.733 + x

# Use the root-finding function from scipy
x_solution = opt.newton(equation, x0=1.0)  # You can provide an initial guess (x0)

# Print the result
print("The solution for x is:", x_solution)
