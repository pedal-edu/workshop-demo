from pedal import *

# You don't have to call verify, it's automatically called by almost every environment
# verify()

# But you can inspect the source code if you want!
if "^" in get_program():
    explain(message="Remember, the ^ is not used as the exponent operator!",
            priority='syntax', label="prevent_caret", title="Do Not Use Caret")