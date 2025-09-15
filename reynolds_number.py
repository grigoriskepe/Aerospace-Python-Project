"""
Script Name: reynolds_number.py
Description: Calculates Reynolds number given velocity, length, density, and viscosity.
"""

def reynolds_number(rho, V, L, mu):
    """
    Calculate Reynolds number.

    Parameters:
        rho (float): Fluid density (kg/m^3).
        V (float): Flow velocity (m/s).
        L (float): Characteristic length (m).
        mu (float): Dynamic viscosity (Pa·s).

    Returns:
        float: Reynolds number (dimensionless).
    """
    return rho * V * L / mu


if __name__ == "__main__":
    rho = 1.225     # kg/m^3 (air at sea level)
    V = 50          # m/s
    L = 1.0         # m (chord length)
    mu = 1.81e-5    # Pa·s (air viscosity at 15°C)

    Re = reynolds_number(rho, V, L, mu)
    print(f"Reynolds Number: {Re:.2e}")
