from bakery import assert_equal

def cube_elements(num1: int, num2: int, num3: int) -> list[int]:
    return [num1**3, num2**3, num3**3]

assert_equal(cube_elements(1, 2, 3), [1, 8, 27])
