from bakery import assert_equal

PI = 3.14159

def calculate_area(radius: float) -> float:
    return radius * radius * PI

def calculate_volume(radius: float, height: float) -> float:
    return calculate_area(radius) * height


assert_equal(calculate_area(1.), PI)
assert_equal(calculate_area(5.), 78.53975)
assert_equal(calculate_area(2.), 12.56636)
assert_equal(calculate_area(0.), 0.)
assert_equal(calculate_volume(1., 2.), 2*PI)
assert_equal(calculate_volume(5., 1.), 78.53975)
assert_equal(calculate_volume(2., 3.1), 38.955716)
assert_equal(calculate_volume(0., 3.1), 0.)
