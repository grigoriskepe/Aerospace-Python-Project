"""
Script Name: dynamic_pressure.py
Description: Calculates the dynamic pressure, given air density and velocity.
"""

def dynamic_pressure(rho, V):
    """

    Parameters:
        rho (float): Air density (kg/m^3).
        V (float): Velocity (m/s).

    Returns:
        float: Dynamic pressure (Pa).
    """
    return 0.5 * rho * V**2


if __name__ == "__main__":
    rho = 1.225   # air density at sea level (kg/m^3)
    V = 50        # velocity in m/s
    q = dynamic_pressure(rho, V)
    print(f"Dynamic Pressure at {V} m/s: {q:.2f} Pa")
