# Truncation and Rounding Error Analysis

This project provides functions to calculate and analyze truncation error, rounding error, and total error for finite difference formulas. It includes a main function to plot the errors using a log-scale and print the optimal h values.

## Overview

In scientific computations, it is crucial to understand the sources of errors and their impact on the results. This project focuses on two types of errors:

- **Truncation Error**: The error introduced by approximating a mathematical procedure.
- **Rounding Error**: The error introduced by the finite precision of floating-point arithmetic.

By analyzing these errors, we can gain insights into the accuracy and stability of numerical methods.

## Features

- **Finite Difference Formulas**: Calculate the derivative of a function using finite difference and central difference formulas.
- **Error Analysis**: Compute truncation error, rounding error, and total error for different step sizes (h).
- **Optimal Step Size**: Determine the optimal step size that minimizes the total error.
- **Visualization**: Plot the errors using a log-scale to visualize their behavior as the step size changes.

## Usage

To run the program, execute the `Truncation and Rounding.py` script. The main function will calculate and plot the errors for different step sizes and print the optimal h values.

```bash
python Truncation and Rounding.py
```

## Conclusions

From the program, we can draw the following conclusions about errors in numerical methods:

1. **Truncation Error**: As the step size (h) decreases, the truncation error generally decreases. However, it may increase again if h becomes too small due to the limitations of floating-point precision.
2. **Rounding Error**: The rounding error increases as the step size (h) decreases because the finite precision of floating-point arithmetic becomes more significant.
3. **Total Error**: The total error is the sum of truncation and rounding errors. There is an optimal step size (h) that minimizes the total error, balancing the trade-off between truncation and rounding errors.

By understanding these errors, we can make informed decisions about the choice of step size and improve the accuracy of numerical computations.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib

Install the dependencies using pip:

```bash
pip install numpy matplotlib
```
