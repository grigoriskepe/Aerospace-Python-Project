"""
Script Name: air_density.py
Description: Calculates air density at a given altitude using a simplified 
             International Standard Atmosphere (ISA) model.
"""

def air_density(altitude_m):
    """
    Compute air density (kg/m^3) at a given altitude in meters using:
        ρ = 1.225 * (1 - 2.25577e-5 * h)**4.25588

    Parameters:
        altitude_m: Altitude in meters (>= 0).

    Returns:
        Air density in kg/m^3.

    Raises:
        ValueError: If altitude_m is negative.
    """
    if altitude_m < 0:
        raise ValueError("Altitude cannot be negative.")
    
    # ISA approximation valid up to the tropopause for quick calculations
    return 1.225 * (1 - 2.25577e-5 * altitude_m) ** 4.25588


if __name__ == "__main__":
    # Example usage: calculate and print air density for selected altitudes
    sample_altitudes = [0, 1000, 5000, 10000, 15000]  # meters
    for h in sample_altitudes:
        print(f"{h:6} m -> {air_density(h):.3f} kg/m^3")
