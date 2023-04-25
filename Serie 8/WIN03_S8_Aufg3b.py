import numpy as np

from WIN03_S8_Aufg3a import trap


def f(r, p):
    return p * 4 * np.pi * (10 ** 3) ** 3 * r ** 2


if __name__ == "__main__":
    vec_r = np.array([0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370])
    vec_p = np.array([13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300])

    mass_wikipedia = 5.9723 * 10 ** 24

    m = f(vec_r, vec_p)
    mass_calculated = trap(vec_r, m)

    print(f"Masse berechnet: {mass_calculated} kg")
    print(f"Masse Wikipedia: {mass_wikipedia} kg")
    abs_error = abs(mass_calculated - mass_wikipedia)
    print(f"Absoluter Fehler: {abs_error} kg")
    print(f"Relativer Fehler {abs_error / mass_wikipedia} %")