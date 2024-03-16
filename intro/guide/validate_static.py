from pedal import *

# Ensure that the function exists with the right name
ensure_function('cube_elements', parameters=[list[int]], returns=list[int])

# Could also just be checking arity instead
ensure_function('cube_elements', arity=1)