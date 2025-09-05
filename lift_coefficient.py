"""
Script Name: lift_coefficient.py
Description: Calculates and plots the lift coefficient (CL) using thin airfoil theory.
"""

import numpy as np
import matplotlib.pyplot as plt


def lift_coefficient(alpha_deg, a0=2 * np.pi):
    """
    Calculate lift coefficient.

    Parameters:
        alpha_deg (float): Angle of attack in degrees.
        a0 (float): Lift curve slope in per radian (default 2π for thin airfoil theory).

    Returns:
        float: Lift coefficient (CL).
    """
    alpha_rad = np.radians(alpha_deg)  # Convert degrees to radians
    return a0 * alpha_rad


def plot_lift_curve(alpha_range=(-10, 15), a0=2 * np.pi):
    """
    Plot the lift curve (CL vs angle of attack).

    Parameters:
        alpha_range (tuple): Minimum and maximum angle of attack in degrees.
        a0 (float): Lift curve slope in per radian.
    """
    alpha_values = np.linspace(alpha_range[0], alpha_range[1], 50)
    cl_values = [lift_coefficient(alpha, a0) for alpha in alpha_values]

    plt.figure(figsize=(8, 5))
    plt.plot(alpha_values, cl_values, "r-")
    plt.axhline(0, color="k", linestyle="--")
    plt.axvline(0, color="k", linestyle="--")
    plt.title("Lift Curve using Thin Airfoil Theory")
    plt.xlabel("Angle of Attack (deg)")
    plt.ylabel("Lift Coefficient (CL)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example usage: Plot lift curve for thin airfoil theory
    plot_lift_curve()