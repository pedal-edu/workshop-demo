from bakery import assert_equal

def cube_elements(num1: int) -> list[int]:
    return [num1**3]

assert_equal(cube_elements(1), [1])
