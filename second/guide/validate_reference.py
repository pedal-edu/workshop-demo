"""
Here is a reference solution for validating the file.
"""
from pedal import *

# Make functions only return
prevent_printing_functions()
ensure_functions_return()

# They must have the function with the right signature
ensure_function('calculate_area', parameters=[float], returns=float)
# They must call the function uniquely at least three times
ensure_function_call('calculate_area', at_least=3)
ensure_called_uniquely('calculate_area', 3)
# Unit tests
unit_test('calculate_area', 
            ([1.0], 3.14159), 
            ([2.], 12.56636), 
            ([0.], 0.0))
# Coverage check
ensure_coverage(.9)
# Have at least 7 tests
ensure_bakery_tests(7)

# They must have the function with the right signature
ensure_function('calculate_volume', parameters=[float, float], returns=float)
# They must call the function uniquely at least four times
ensure_function_call('calculate_volume', at_least=4, message="Have at least four unit tests for `calculate_volume`.")
ensure_called_uniquely('calculate_volume', 4)
# Unit tests
unit_test("calculate_volume",
            ([1., 2.], 6.28318),
            ([5., 1.], 78.53975),
            ([2., 3.1], 38.955716),
            ([0., 0.], 0.),
            ([0., 100.], 0.),
            ([100., 0.], 0.))

# There are many other CAIT helper functions available to you, such as
# https://pedal-edu.github.io/pedal/developers/tools/cait.html#pedal.cait.find_node.find_function_calls
calculate_volume = find_function_definition('calculate_volume')
if not find_function_calls('calculate_area', root=calculate_volume):
    gently("You need to use `calculate_area` inside of `calculate_volume`.",
            label="not_using_calculate_area", title="Not Using calculate_area")
