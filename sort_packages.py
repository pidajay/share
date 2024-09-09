from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    VOLUME_TOLERANCE: float = 1e6
    DIM_TOLERANCE: float = 150.0
    MASS_TOLERANCE: float = 20.0

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package based on its dimensions and mass.

    Parameters:
    width (float): The width of the package in cm.
    height (float): The height of the package in cm.
    length (float): The length of the package in cm.
    mass (float): The mass of the package in kg.

    Returns:
    str: The category of the package ('REJECTED', 'SPECIAL', 'STANDARD').
    """
    volume = width * height * length
    bulky  = volume >= Constants.VOLUME_TOLERANCE or any(i >= Constants.DIM_TOLERANCE for i in [width, height, length])
    heavy = mass >= Constants.MASS_TOLERANCE
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    
# Example usage
if __name__ == "__main__":
    width = 10
    height = 10
    length = 100
    mass = 100
    print(sort(width, height, length, mass))  # Output: 'SPECIAL'