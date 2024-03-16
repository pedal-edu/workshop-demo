from pedal import *

unit_test('cube_elements',
            ([[1, 2, 3]], [1, 8, 27]),
            ([[1]], [1]),
            ([[4, 4, 4]], [64, 64, 64]),
            ([[0]], [0]),
            ([[]], []))



# Alternative syntax
with unit_test('cube_elements'):
    assert_equal(call('cube_elements', [1, 2, 3]), [1, 8, 27])
    assert_equal(call('cube_elements', [1]), [1])
    assert_equal(call('cube_elements', [4, 4, 4]), [64, 64, 64])
    assert_equal(call('cube_elements', [0]), [0])
    assert_equal(call('cube_elements', []), [])
    
# And you can run them individually too
assert_equal(call('cube_elements', [1, 2, 3]), [1, 8, 27])