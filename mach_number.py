"""
Script Name: mach_number.py
Description: Calculates Mach number given velocity and speed of sound.
"""

def mach_number(V, a=343):
    """

    Parameters:
        V (float): Velocity of object (m/s).
        a (float): Speed of sound (m/s), default 343 m/s at 20°C at sea level.

    Returns:
        float: Mach number.
    """
    return V / a


if __name__ == "__main__":

    V = 250      # velocity in m/s
    a = 343      # speed of sound (m/s)
    M = mach_number(V, a)
    print(f"Mach number at {V} m/s: {M:.2f}")
