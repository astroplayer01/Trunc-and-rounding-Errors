import numpy as np

# Define the function whose derivative we are approximating
def f(x):
    return np.sin(x)

# Define the analytical derivative of the function
def df(x):
    return np.cos(x)

# Define the finite difference approximations
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Define the error calculations
def truncation_error(approx, exact):
    return np.abs(approx - exact)

# Main function
def main():
    x = np.pi / 4  # Example point where we are calculating the derivative
    h_values = [0.1, 0.01, 0.001, 0.0001]  # Different step sizes

    print(f"{'h':<10}{'Forward Error':<20}{'Backward Error':<20}{'Central Error':<20}")
    for h in h_values:
        exact_value = df(x)
        forward_approx = forward_difference(f, x, h)
        backward_approx = backward_difference(f, x, h)
        central_approx = central_difference(f, x, h)

        forward_error = truncation_error(forward_approx, exact_value)
        backward_error = truncation_error(backward_approx, exact_value)
        central_error = truncation_error(central_approx, exact_value)

        print(f"{h:<10}{forward_error:<20}{backward_error:<20}{central_error:<20}")

if __name__ == "__main__":
    main()
