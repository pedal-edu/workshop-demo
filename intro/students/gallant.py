def cube_elements(numbers: list[int]) -> list[int]:
    i = 0
    while i < len(numbers):
        numbers[i] = numbers[i]**3
        i += 1
    return numbers
