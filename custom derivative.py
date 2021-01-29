# Define a function that you want to differentiate:
import sympy as sp


x = sp.symbols('x')

def k(x):
    return x**3

# Input the order to which you want to differentiate:


n = int(input("What is the order to which you want to differentiate this function?"))

# print(n)

# Add n number of x's to list


num_of_derivs = 'x'*n

diff_k = sp.diff(k(x), num_of_derivs)


print(diff_k)

# for each_deriv in range(1, n+1)

# Split the list into individual strings
# Enter the x's into the deriv funtion

# Place the input into the differentiating function

# desired_deriv = sp.diff(k(x), n)

# Print a list of all the derivatives
