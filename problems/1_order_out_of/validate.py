from pedal import *

ensure_literal("order out of")
prevent_ast("Str", at_most=1)
ensure_ast("Subscript", at_least=2)
prevent_ast("Subscript", at_most=5)
ensure_function_call("print")

assert_not_output(student, "out of order ", exact_strings=True,
                    message="There's an extra space at the end!",
                    label="printing_extra_space")
assert_output(student, "out of order", exact_strings=True)
