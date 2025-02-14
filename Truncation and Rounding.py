"""
This module provides functions to calculate and analyze truncation error, rounding error,
and total error for finite difference formulas. It also includes a main function to plot
the errors using a log-scale and print the optimal h values.
"""

#imports needed to run the code
import math
import numpy as np
from typing import Callable
import matplotlib.pyplot as plt

def f(x: float) -> float:
    """
    Returns the sine of x.
    
    Args:
        x (float): Input value.
    
    Returns:
        float: Sine of x.
    """
    return math.sin(x)

def df_One(x: float, h: float) -> float:
    """
    Returns the finite difference approximation of the derivative of f at x using step size h.
    
    Args:
        x (float): Input value.
        h (float): Step size.
    
    Returns:
        float: Finite difference approximation of the derivative.
    """
    return (f(x + h) - f(x)) / h

def df_Two(x: float, h: float) -> float:
    """
    Returns the central difference approximation of the derivative of f at x using step size h.
    
    Args:
        x (float): Input value.
        h (float): Step size.
    
    Returns:
        float: Central difference approximation of the derivative.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def df_Real(x: float) -> float:
    """
    Returns the actual derivative of f at x.
    
    Args:
        x (float): Input value.
    
    Returns:
        float: Actual derivative of f.
    """
    return math.cos(x)

def ddf(x: float) -> float:
    """
    Returns the second derivative of f at x.
    
    Args:
        x (float): Input value.
    
    Returns:
        float: Second derivative of f.
    """
    return -math.sin(x)

def truncation_error(x: float, h: float, func: Callable[[float], float]) -> float:
    """
    Returns the truncation error for the given finite difference formula.
    
    Args:
        x (float): Input value.
        h (float): Step size.
        func (Callable[[float], float]): Finite difference function.
    
    Raises:
        ValueError: If the function is not recognized.
    
    Returns:
        float: Truncation error.
    """
    if func is df_One:
        return (h / 2) * ddf(x)
    elif func is df_Two:
        return ((h ** 2) / 6) * ddf(x)
    else:
        raise ValueError("Invalid function for truncation error calculation")

def rounding_error() -> float:
    """
    Returns the rounding error for the given finite difference formula.
    
    Args:
        None
    
    Returns:
        float: Rounding error.
    """
    return np.finfo(float).eps

def total_error(x: float, h: float, func: Callable[[float], float]) -> float:
    """
    Returns the total error (sum of truncation error and rounding error) for the given finite difference formula.
    
    Args:
        x (float): Input value.
        h (float): Step size.
        func (Callable[[float], float]): Finite difference function.
    
    Returns:
        float: Total error.
    """
    trunc_error = truncation_error(x, h, func)
    round_error = rounding_error()
    return trunc_error + round_error

def main() -> None:
    """
    Main function to calculate and plot truncation error, rounding error, and total error
    for df_One and df_Two using a log-scale. Also prints the optimal h values.
    """
    x = 1
    h = 0.5
    
    # Lists to store h values and errors
    h_values = []
    trunc_errors_one = []
    trunc_errors_two = []
    round_errors_one = []
    round_errors_two = []
    total_errors_one = []
    total_errors_two = []
    
    # Loop to calculate errors for different h values
    for i in range(16):
        h = 10 ** -(i + 1)
        h_values.append(h)
        
        y_one = df_One(x, h)
        y_two = df_Two(x, h)
        
        trunc_one = truncation_error(x, h, df_One)
        trunc_two = truncation_error(x, h, df_Two)
        
        round_one = rounding_error()
        round_two = rounding_error()
        
        total_one = total_error(x, h, df_One)
        total_two = total_error(x, h, df_Two)
        
        trunc_errors_one.append(abs(trunc_one))
        trunc_errors_two.append(abs(trunc_two))
        round_errors_one.append(abs(round_one))
        round_errors_two.append(abs(round_two))
        total_errors_one.append(abs(total_one))
        total_errors_two.append(abs(total_two))
        
        # Print errors for current h value
        print(f"h: {h:.1e}, df_One: {y_one:.1e}, df_Two: {y_two:.1e}")
        print(f"Truncation Error df_One: {trunc_one:.1e}, df_Two: {trunc_two:.1e}")
        print(f"Rounding Error df_One: {round_one:.1e}, df_Two: {round_two:.1e}")
        print(f"Total Error df_One: {total_one:.1e}, df_Two: {total_two:.1e}")
        print()
    
    # Find optimal h values
    optimal_index_one = np.argmin(total_errors_one)
    optimal_index_two = np.argmin(total_errors_two)
    optimal_h_one = h_values[optimal_index_one]
    optimal_h_two = h_values[optimal_index_two]
    
    # Print optimal h values and corresponding errors
    print(f"Optimal h for df_One: {optimal_h_one:.1e} at iteration {optimal_index_one + 1}")
    print(f"Truncation Error: {trunc_errors_one[optimal_index_one]:.1e}, Rounding Error: {round_errors_one[optimal_index_one]:.1e}, Total Error: {total_errors_one[optimal_index_one]:.1e}")
    
    print(f"Optimal h for df_Two: {optimal_h_two:.1e} at iteration {optimal_index_two + 1}")
    print(f"Truncation Error: {trunc_errors_two[optimal_index_two]:.1e}, Rounding Error: {round_errors_two[optimal_index_two]:.1e}, Total Error: {total_errors_two[optimal_index_two]:.1e}")
    
    # Plot errors using log-scale
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.loglog(h_values, trunc_errors_one, label='Truncation Error')
    plt.loglog(h_values, round_errors_one, label='Rounding Error')
    plt.loglog(h_values, total_errors_one, label='Total Error')
    plt.xlabel('log10 h')
    plt.ylabel('log10 |error|')
    plt.title('Error Analysis for df_One')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.loglog(h_values, trunc_errors_two, label='Truncation Error')
    plt.loglog(h_values, round_errors_two, label='Rounding Error')
    plt.loglog(h_values, total_errors_two, label='Total Error')
    plt.xlabel('log10 h')
    plt.ylabel('log10 |error|')
    plt.title('Error Analysis for df_Two')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()