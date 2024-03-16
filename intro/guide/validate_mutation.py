from pedal import *

run("""
numbers = [1, 2, 3]
cube_elements(numbers)
""")

if evaluate('numbers') == [1, 8, 27]:
    gently("You are modifying the list, instead of returning a new list.",
            title="Mutating Parameter", label="mutating_parameter")