## This is the "long" starting version, which you would need if there 
## isn't an appropriate environment

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
