from pedal import *
from dataclasses import dataclass

prevent_printing_functions()
ensure_functions_return()

# Prevent them from writing `bird.can_fly == False`
prevent_operator("is", message="You do not need the `is` operator.")
prevent_operator("is not", message="You do not need the `is not` operator.")
prevent_operator("==", message="You do not need the `==` operator.")
prevent_operator("!=", message="You do not need the `!=` operator.")

@dataclass
class Bird:
    name: str
    can_fly: bool
    region: str


# Special helper function that can check the student's dataclass definition
ensure_dataclass(Bird, priority='instructor')
assert_is_instance(evaluate("Bird"), type)

ensure_function('first_land_bird', 1, ['list[Bird]'], str)
ensure_function_callable('first_land_bird')

ensure_coverage(.9)
ensure_cisc108_tests(2)
ensure_function_call('Bird', 2)
ensure_called_uniquely('first_land_bird', 2)

# I create a bunch of instances
with CommandBlock() as context:
    call('Bird', 'roc', True, 'Nowhere', target='mythical_roc')
    call('Bird', 'rock', False, 'Everywhere', target="flying_rock")
    call('Bird', 'toucan', True, 'Americas', target='toucan')
    call('Bird', 'parrot', True, 'Americas', target='parrot')
    call('Bird', 'ostrich', False, 'Africa', target='ostrich')
    call('Bird', 'swallow', True, 'European', target='european_swallow')
    call('Bird', 'swallow', True, 'African', target='african_swallow')

# The context will be provided when the tests fail!
unit_test('first_land_bird', 
            ([[]], "Flew the coop"),
            ('[mythical_roc, toucan, parrot]', "Flew the coop"),
            ('[flying_rock, ostrich]', "rock"),
            ('[toucan, parrot, ostrich]', "ostrich"),
            ('[mythical_roc, flying_rock, parrot]', "rock"),
            ('[european_swallow, african_swallow]', "Flew the coop"),
            ('[european_swallow, african_swallow, flying_rock]', "rock"),
            context=context
)

