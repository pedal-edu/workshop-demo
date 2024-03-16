from pedal import *

# Check for recursion, list comprehensions, while loops, etc.
prevent_advanced_iteration(allow_for=True)

# Check if they use a ^ instead of ** for exponentiation
if "^" in get_program():
    explain("Remember, the ^ is not used as the exponent operator!",
            priority='syntax', label="prevent_caret", title="Do Not Use Caret")

# Prevent them from using + to concatenate lists
prevent_operation("+", message="You cannot add elements using the `+` operator. "
                    "Instead, you need to use the `append` method.")

# Make sure they definitely do use the append method
ensure_function_call('append')

# They HAVE to use a for loop
ensure_ast('For')

# No printing inside of functions
prevent_printing_functions()

# Functions must return
ensure_functions_return()

# They better define the function with the right type!
ensure_function('cube_elements', parameters=[list[int]], returns=list[int])

# Old-style checks for at least two calls
# Can also use the ensure_bakery_tests(3) function
ensure_function_call('cube_elements', at_least=3)
# Their tests should achieve 90% coverage
ensure_coverage(.9)
# Check that their tests are all unique
ensure_called_uniquely('cube_elements', 3)

# Actual unit tests
unit_test('cube_elements',
            ([[1, 2, 3]], [1, 8, 27]),
            ([[1]], [1]),
            ([[4, 4, 4]], [64, 64, 64]),
            ([[0]], [0]),
            ([[]], []))

# Check for a specific mistake
if call("cube_elements", [1,2,3]) == 6:
    gently("You have summed the list instead of cubing each element.",
            title="Wrong Algorithm", label="summing_instead_of_cubing")

# Check for mutation
run("""
numbers = [1, 2, 3]
cube_elements(numbers)
""")
if evaluate('numbers') == [1, 8, 27]:
    gently("You are modifying the list, instead of returning a new list.",
            title="Mutating Parameter", label="mutating_parameter")
    

# Check that they put the FOR loop inside the function
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