"""Calculate microstrip line width based on different formulas"""
import math


def calculate_width(
        target_impedance: float,
        permittivity: float,
        dielectric_thickness: float,
        metal_thickness: float
) -> float:
    power = target_impedance * (math.sqrt(permittivity + math.sqrt(2))) / 87
    return (7.48 * dielectric_thickness) / pow(math.e, power) - 1.25 * metal_thickness


def calculate_width_2(
        target_impedance: float,
        permittivity: float,
        dielectric_thickness: float,
        metal_thickness: float
) -> float:
    power = target_impedance * (math.sqrt(permittivity + 1.41)) / 87
    return (5.98 * dielectric_thickness / pow(math.e, power) - metal_thickness) / 0.8


if __name__ == '__main__':
    Z0 = 50
    perm = 3.4
    d_thickness = 4.25
    m_thickness = 1

    width = calculate_width(Z0, perm, d_thickness, m_thickness)
    width_mm = round(width * 0.0254, 3)
    width = round(width, 3)
    print('[1] w in mils = ', width, 'w in mm =', width_mm)

    width = calculate_width_2(Z0, perm, d_thickness, m_thickness)
    width_mm = round(width * 0.0254, 3)
    width = round(width, 3)
    print('[2] w in mils = ', width, 'w in mm =', width_mm)
