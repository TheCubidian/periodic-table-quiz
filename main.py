import random
symbols = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",
"Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni",
"Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc",
"Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce",
"Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta",
"W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra",
"Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
"Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og")

elements = ("Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen",
"Fluorine", "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorous", "Sulfur",
"Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
"Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic",
"Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum",
"Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony",
"Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
"Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium",
"Ytterbium", "Lutelium", "Halfnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum",
"Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium",
"Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium",
"Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium",
"Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium",
"Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson")

questions = None
wrong = 0
right = 0
index = random.randint(0, 117)
used = []
used.append(index)
while True:
    questions = input("\nDo you want to be tested on the symbols of named elements, or the elements of named symbols? 1/2 ")
    if questions == "1" or questions == "2":
        break
if questions == "1":
    while True:
        answer = input(f"What is the symbol for the following element: {elements[index]}? ")
        if answer == symbols[index]:
            print("Correct!")
            right += 1
            used.append(index)
        else:
            print(f"Wrong! The correct answer was {symbols[index]}.")
            wrong += 1
            used.append(index)
        while index in used:
            index = random.randint(0, 117)
            if len(used) == 119:
                print(f"You have completed the quiz on all 118 elements in the periodic table on mode {questions}! You got {right} right and {wrong} wrong.")
                exit()
else:
    while True:
        answer = input(f"What is the name of the element with the following symbol: {symbols[index]}? ").lower()
        if answer.lower() == elements[index].lower():
            print("Correct!")
            right += 1
            used.append(index)
        else:
            print(f"Wrong! The correct answer was {elements[index]}.")
            wrong += 1
            used.append(index)
        while index in used:
            index = random.randint(0, 117)
            if len(used) == 119:
                print(f"You have completed the quiz on all 118 elements in the periodic table on mode {questions}! You got {right} right and {wrong} wrong.")
                exit()