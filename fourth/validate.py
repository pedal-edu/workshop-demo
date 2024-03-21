from pedal import *

clear_output()
run(inputs=["1"])
assert_output_contains(student, "1.2")

clear_output()
run(inputs=["10"])
assert_output_contains(student, "12.0")