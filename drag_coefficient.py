"""
Script Name: drag_coefficient.py
Description: Calculates drag coefficient given drag force, dynamic pressure, and reference area.
"""

def drag_coefficient(D, q, S):
    """Calculate drag coefficient.

    Parameters:
        D (float): Drag force (N).
        q (float): Dynamic pressure (Pa).
        S (float): Reference area (m^2).

    Returns:
        float: Drag coefficient (dimensionless).
    """
    return D / (q * S)


if __name__ == "__main__":
    # Example usage
    D = 500.0   # drag force in N
    q = 1500.0  # dynamic pressure in Pa
    S = 20.0    # reference area in m^2

    CD = drag_coefficient(D, q, S)
    print(f"Drag coefficient: {CD:.3f}")
