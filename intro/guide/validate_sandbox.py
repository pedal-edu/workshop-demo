from pedal import *

# Alternative syntax
with unit_test('cube_elements'):
    cube_elements = get_function('cube_elements')
    assert_equal(cube_elements([1, 2, 3]), [1, 8, 27])
    assert_equal(cube_elements([1]), [1])
    assert_equal(cube_elements([4, 4, 4]), [64, 64, 64])
    assert_equal(cube_elements([0]), [0])
    assert_equal(cube_elements([]), [])