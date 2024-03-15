from bakery import assert_equal

def cube_elements(numbers: list[int]) -> list[int]:
    cubed = []
    for number in numbers:
        cubed.append(number**3)
    return cubed

assert_equal(cube_elements([1, 2, 3]), [1, 8, 27])
assert_equal(cube_elements([4, 5, 6, 0, 0]), [64, 125, 216, 0, 0])
assert_equal(cube_elements([]), [])


def cube_elements(numbers: list[int]) -> list[int]:
    i = 0
    while i < len(numbers):
        numbers[i] = numbers[i]**3
        i += 1
    return numbers


def cube_elements(numbers: list[int]) -> list[int]:
    numbers = [1, 2, 3]
    print(numbers ^ 3)


numbers_norm = [1,2,3]
def cube_elements(number: list[int]) -> list[int]:
    cubed_number = number**3
    return cubed_number
numbers_cubed = []
for numbers in numbers_cubed:
    numbers_cubed = cube_elements.append(numbers)
    print(numbers_cubed)
    
    
#----------------------------------------------

# Always start by importing Pedal
from pedal import *

# Load the students' code
student_code = "print('Hello world!')"
contextualize_report(student_code)

# Check their source code for syntax errors
verify()
# Run their code
student = run(student_code)

# ... More instructor logic can go here ...

# Resolve output and print
from pedal.resolvers import print_resolve
print_resolve()