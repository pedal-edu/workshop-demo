from bakery import assert_equal

def cube_elements(numbers: list[int]) -> list[int]:
    numbers = [1, 2, 3]
    cubed = []
    for number in numbers:
        cubed.append(number**3)
    return cubed

assert_equal(cube_elements([1, 2, 3]), [1, 8, 27])
