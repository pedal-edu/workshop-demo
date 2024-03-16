from pedal import *

found_function = find_match("def cube_elements(): pass")
found_loop = find_match("for ___ in ___: pass")
if found_function and found_loop:
    loop_inside_function = find_match(
        "def cube_elements():\n"
        " for ___ in ___:\n"
        "  pass"
    )
    if not loop_inside_function:
        explain("Your for loop is not inside of your function.")