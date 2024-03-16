from pedal import *

prevent_ast("While")
ensure_ast("For")
prevent_ast("For", at_most=1)