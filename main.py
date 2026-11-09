#ICT 10 Skills Test: Non-Metal Elements
from pyscript import document, display

nonmetals = {
    "H": ("Hydrogen", 1, "1.008"),
    "C": ("Carbon", 6, "12.011"),
    "N": ("Nitrogen", 7, "14.007"),
    "O": ("Oxygen", 8, "15.999"),
    "F": ("Fluorine", 9, "18.998"),
    "P": ("Phosphorus", 15, "30.974"),
    "S": ("Sulfur", 16, "32.06"),
    "Cl": ("Chlorine", 17, "35.45"),
    "Se": ("Selenium", 34, "78.971"),
    "Br": ("Bromine", 35, "79.904"),
    "I": ("Iodine", 53, "126.904"),
    "He": ("Helium", 2, "4.0026"),
    "Ne": ("Neon", 10, "20.180"),
    "Ar": ("Argon", 18, "39.948"),
    "Kr": ("Krypton", 36, "83.798"),
    "Xe": ("Xenon", 54, "131.293"),
    "Rn": ("Radon", 86, "222"),
}

def find_element(event):
    symbol = document.getElementById("symbol").value.strip().capitalize()

    name, number, mass = nonmetals.get(
        symbol,
        ("This element does not exist in the nonmetals list.", "", "")
    )

    result = (
        f"Element Symbol: {symbol or '—'}\n"
        f"Element Name: {name}\n"
        f"Atomic Number: {number}\n"
        f"Atomic Mass: {mass}"
    )

    display(result, target="result")