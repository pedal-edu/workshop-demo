from bakery import assert_equal

def cube_elements(numbers: list[int]) -> list[int]:
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**3
    return numbers

assert_equal(cube_elements([1, 2, 3]), [1, 8, 27])
assert_equal(cube_elements([4, 5, 6, 0]), [64, 125, 216, 0])
assert_equal(cube_elements([]), [])
