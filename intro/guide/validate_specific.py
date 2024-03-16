from pedal import *


assert_not_equal(call('cube_elements', [1, 2, 3]), 6,
                message="You have summed the list instead of cubing each element.",
                title="Wrong Algorithm", label="summing_instead_of_cubing")


assert_not_equal(call('cube_elements', [1, 2, 3]), 36,
                message="You have calculated the sum of all the cubes; but I wanted you to make a LIST of the cubes.",
                title="Wrong Algorithm", label="summing_instead_of_mapping")