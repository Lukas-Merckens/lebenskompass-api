import swisseph as swe
import datetime
import os

# Setze Pfad zu den Ephemeriden-Dateien
EPHE_PATH = os.path.join(os.path.dirname(__file__), "ephe")
swe.set_ephe_path(EPHE_PATH)

# Definierte Planeten inkl. Node (Mondknoten)
PLANETS = {
    "sun": swe.SUN,
    "moon": swe.MOON,
    "mercury": swe.MERCURY,
    "venus": swe.VENUS,
    "mars": swe.MARS,
    "jupiter": swe.JUPITER,
    "saturn": swe.SATURN,
    "uranus": swe.URANUS,
    "neptune": swe.NEPTUNE,
    "pluto": swe.PLUTO,
    "mean_node": swe.MEAN_NODE,  # ☊
}

def calculate_planet_positions(year, month, day, hour, minute, second, timezone_offset=0.0):
    jd = swe.julday(year, month, day, hour + minute / 60 + second / 3600 - timezone_offset)
    positions = {}

    for name, planet in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet)
        positions[name] = round(pos[0], 6)

    # Erde = gegenüberliegende Position der Sonne
    positions["earth"] = (positions["sun"] + 180) % 360

    # Südlicher Mondknoten ☋ = ☊ + 180°
    positions["south_node"] = (positions["mean_node"] + 180) % 360

    return positions

# Beispielnutzung (kann später entfernt werden):
if __name__ == "__main__":
    result = calculate_planet_positions(1966, 12, 2, 22, 54, 0, timezone_offset=1.0)
    for body, pos in result.items():
        print(f"{body}: {pos:.6f}°")
