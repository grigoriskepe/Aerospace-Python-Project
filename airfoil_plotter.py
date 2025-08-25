"""
Script Name: airfoil_plotter.py
Description: Generates and plots the coordinates of a NACA 4-digit airfoil.
"""

import numpy as np
import matplotlib.pyplot as plt


def naca4(m, p, t, num_points=100):
    """
    Generate the coordinates of a 4-digit NACA airfoil.

    Parameters:
        m (float): Maximum camber (first digit) / 100.
        p (float): Position of max camber (second digit) / 10.
        t (float): Maximum thickness (last two digits) / 100.
        num_points (int): Number of coordinate points.

    Returns:
        tuple: (x, y) coordinates of the airfoil shape.
    """
    x = np.linspace(0, 1, num_points)

    # Thickness distribution
    yt = 5 * t * (
        0.2969 * np.sqrt(x)
        - 0.1260 * x
        - 0.3516 * x**2
        + 0.2843 * x**3
        - 0.1015 * x**4
    )

    # Camber line and slope
    yc = np.where(
        x < p,
        m / (p**2) * (2 * p * x - x**2),
        m / ((1 - p) ** 2) * ((1 - 2 * p) + 2 * p * x - x**2),
    )

    dyc_dx = np.where(
        x < p,
        2 * m / (p**2) * (p - x),
        2 * m / ((1 - p) ** 2) * (p - x),
    )

    theta = np.arctan(dyc_dx)

    # Upper and lower surfaces
    xu = x - yt * np.sin(theta)
    yu = yc + yt * np.cos(theta)

    xl = x + yt * np.sin(theta)
    yl = yc - yt * np.cos(theta)

    return np.concatenate([xu[::-1], xl[1:]]), np.concatenate([yu[::-1], yl[1:]])


def plot_airfoil(code="2412"):
    """
    Plot a 4-digit NACA airfoil given its code.

    Parameters:
        code (str): 4-digit NACA code (e.g., "2412").
    """
    if len(code) != 4 or not code.isdigit():
        raise ValueError("NACA code must be 4 digits (e.g., '2412').")

    m = int(code[0]) / 100
    p = int(code[1]) / 10
    t = int(code[2:]) / 100

    x, y = naca4(m, p, t)

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, "b-")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(f"NACA {code} Airfoil")
    plt.xlabel("x (chord)")
    plt.ylabel("y (thickness)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example usage: plot the classic NACA 2412 airfoil
    plot_airfoil("2412")

