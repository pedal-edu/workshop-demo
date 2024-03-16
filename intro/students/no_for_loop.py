from bakery import assert_equal

def cube_elements(numbers: list[int]) -> list[int]:
    cubed = []
    if len(numbers) > 0:
        cubed.append(numbers[0]**3)
    if len(numbers) > 1:
        cubed.append(numbers[1]**3)
    if len(numbers) > 2:
        cubed.append(numbers[2]**3)
    if len(numbers) > 3:
        cubed.append(numbers[3]**3)
    if len(numbers) > 4:
        cubed.append(numbers[4]**3)
    if len(numbers) > 5:
        cubed.append(numbers[5]**3)
    return cubed

assert_equal(cube_elements([1, 2, 3]), [1, 8, 27])
assert_equal(cube_elements([4, 5, 6, 0]), [64, 125, 216, 0])
assert_equal(cube_elements([]), [])
