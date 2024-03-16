from bakery import assert_equal

def cube_elements(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

assert_equal(cube_elements([1, 2, 3]), 6)
assert_equal(cube_elements([4, 5, 6, 0]), 15)
assert_equal(cube_elements([]), 0)
