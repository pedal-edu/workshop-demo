from bakery import assert_equal

def cube_elements(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number**3
    return total

assert_equal(cube_elements([1, 2, 3]), 13)
assert_equal(cube_elements([4, 5, 6, 0]), 4**3 + 5**3 + 6**3)
assert_equal(cube_elements([]), 0)
